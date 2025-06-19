# music/handlers/play.py

import os
import yt_dlp
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream.input_file import InputAudioFile

from config import SESSION_STRING, API_ID, API_HASH
from pytgcalls.types.stream import StreamAudioEnded

app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)
pytgcalls = PyTgCalls(app)

# Song download folder
if not os.path.exists("downloads"):
    os.makedirs("downloads")

queue = {}

# YouTube download function
def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return f"downloads/{info['title']}.mp3"

# Play command
@app.on_message(filters.command("play") & filters.group)
async def play(_, message: Message):
    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply("🎵 YouTube link do ya audio reply karo.")

    chat_id = message.chat.id

    if message.reply_to_message and message.reply_to_message.audio:
        audio = await message.reply_to_message.download(file_name="downloads/")
        await join_and_stream(chat_id, audio)
        return await message.reply("🎶 Playing telegram audio!")

    url = message.text.split(None, 1)[1]
    msg = await message.reply("🔍 Downloading...")
    audio_file = download_audio(url)
    await join_and_stream(chat_id, audio_file)
    await msg.edit("✅ Playing!")

# Function to join & stream
async def join_and_stream(chat_id, audio_path):
    await pytgcalls.join_group_call(
        chat_id,
        InputAudioStream(
            InputAudioFile(audio_path),
        )
    )
    queue[chat_id] = audio_path

# Skip command
@app.on_message(filters.command("skip") & filters.group)
async def skip(_, message: Message):
    chat_id = message.chat.id
    if chat_id in queue:
        os.remove(queue[chat_id])
        await pytgcalls.leave_group_call(chat_id)
        del queue[chat_id]
        await message.reply("⏭️ Skipped!")
    else:
        await message.reply("❌ No song playing.")

# Stop command
@app.on_message(filters.command("stop") & filters.group)
async def stop(_, message: Message):
    chat_id = message.chat.id
    if chat_id in queue:
        os.remove(queue[chat_id])
        del queue[chat_id]
    await pytgcalls.leave_group_call(chat_id)
    await message.reply("⛔ Stopped music.")

# Auto clear finished song
@pytgcalls.on_stream_end()
async def auto_leave(_, update: StreamAudioEnded):
    chat_id = update.chat_id
    if chat_id in queue:
        os.remove(queue[chat_id])
        del queue[chat_id]
        await pytgcalls.leave_group_call(chat_id)

