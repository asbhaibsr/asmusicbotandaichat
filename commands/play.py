from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from helpers.player import stream_music

from config import API_ID, API_HASH, BOT_TOKEN

app = Client("MusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(app)

@app.on_message(filters.command("play") & filters.group)
async def play_handler(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("❗ Example: `/play Ram Siya Ram`")
    
    query = " ".join(message.command[1:])
    await stream_music(client, pytgcalls, message, query)
