import os
import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.stream import StreamAudioEnded
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pyrogram.types import Message
from pymongo import MongoClient
from helpers.ai import get_ai_reply
from helpers.music import MusicPlayer
from pyrogram.idle import idle

# Load environment variables
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SESSION_STRING = os.environ.get("SESSION_STRING")
OWNER_ID = int(os.environ.get("OWNER_ID"))
MONGO_URL = os.environ.get("MONGO_URL")

# MongoDB setup for music queue
db_client = MongoClient(MONGO_URL)
music_db = db_client["musicbot"]
music_col = music_db["queue"]

# Pyrogram Clients
bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client(session_string=SESSION_STRING, api_id=API_ID, api_hash=API_HASH)
call = PyTgCalls(user)

# AI chat and memory
aichat_on = set()
ai_memory = {}

# Music Player
music_player = MusicPlayer(call, music_col)

# Start command
@bot.on_message(filters.command("start"))
async def start(_, msg: Message):
    await msg.reply("🤖 Bot Active! Use /play <song name> or /aichat on")

# AI chat toggle
@bot.on_message(filters.command("aichat") & filters.group)
async def toggle_ai(_, msg):
    if len(msg.command) < 2:
        return await msg.reply("Usage: /aichat on or /aichat off")
    action = msg.command[1].lower()
    chat_id = msg.chat.id
    if action == "on":
        aichat_on.add(chat_id)
        await msg.reply("💬 AI Chat enabled in this group!")
    elif action == "off":
        aichat_on.discard(chat_id)
        await msg.reply("🔇 AI Chat disabled in this group.")

# AI message handler
@bot.on_message(filters.text & filters.group & ~filters.command(["aichat", "play", "pause", "stop"]))
async def ai_reply(_, msg):
    if msg.chat.id not in aichat_on:
        return
    if msg.reply_to_message and msg.reply_to_message.from_user.id != (await bot.get_me()).id:
        return
    user_msg = msg.text
    chat_id = str(msg.chat.id)
    if chat_id not in ai_memory:
        ai_memory[chat_id] = []
    ai_memory[chat_id].append(user_msg)
    ai_memory[chat_id] = ai_memory[chat_id][-5:]
    reply = await get_ai_reply(ai_memory[chat_id])
    await msg.reply(reply)

# Music commands
@bot.on_message(filters.command("play") & filters.group)
async def play_cmd(_, msg):
    query = msg.text.split(None, 1)
    if len(query) < 2:
        return await msg.reply("Please provide a song name.")
    song_name = query[1]
    await music_player.play_song(msg.chat.id, song_name, msg)

@bot.on_message(filters.command("pause") & filters.group)
async def pause_cmd(_, msg):
    await music_player.pause(msg.chat.id, msg)

@bot.on_message(filters.command("stop") & filters.group)
async def stop_cmd(_, msg):
    await music_player.stop(msg.chat.id, msg)

# Start everything
async def main():
    await user.start()
    await call.start()
    await bot.start()
    print("Bot is running...")
    await idle()

if __name__ == "__main__":
    asyncio.run(main())
