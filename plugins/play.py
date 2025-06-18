from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS
from utils.music_stream import stream_audio, stream_video

@Client.on_message(filters.command(["play", "vplay", "stream"]) & filters.group)
async def play_handler(client, message: Message):
    user = message.from_user.mention if message.from_user else "User"
    if not message.reply_to_message and len(message.command) < 2:
        return await message.reply("🎵 Song ka naam ya link do jaaan!")

    query = ""
    if message.reply_to_message and message.reply_to_message.audio:
        audio = message.reply_to_message.audio
        await stream_audio(client, message, audio.file_id, title=audio.title)
        return
    elif message.reply_to_message and message.reply_to_message.text:
        query = message.reply_to_message.text
    else:
        query = " ".join(message.command[1:])

    if message.command[0] == "vplay":
        await stream_video(client, message, query)
    else:
        await stream_audio(client, message, query)

@Client.on_message(filters.command("stop") & filters.group & filters.user(SUDO_USERS))
async def stop_handler(client, message: Message):
    from pytgcalls import idle
    try:
        await idle()  # end music stream
        await message.reply("⏹️ Music band kar diya gaya!")
    except Exception as e:
        await message.reply(f"Error: {e}")
