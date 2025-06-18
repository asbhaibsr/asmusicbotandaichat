import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputStream, AudioPiped
from config import API_ID, API_HASH, BOT_TOKEN
from music import play_music
from ai import generate_ai_reply, ai_enabled_users

app = Client("music_ai_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(app)


@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    await message.reply_text("👋 Hello! I’m your AI-Powered Music Bot.\nUse /play <song name> to play music.\nUse /ai to turn AI chat on or off.")

@app.on_message(filters.command("ai") & filters.private)
async def toggle_ai(client, message: Message):
    user_id = message.from_user.id
    if user_id in ai_enabled_users:
        ai_enabled_users.remove(user_id)
        await message.reply_text("🤖 AI chat disabled.")
    else:
        ai_enabled_users.add(user_id)
        await message.reply_text("🤖 AI chat enabled.")

@app.on_message(filters.text & filters.private)
async def private_chat(client, message: Message):
    user_id = message.from_user.id
    if user_id in ai_enabled_users:
        reply = await generate_ai_reply(message.text, user_id)
        await message.reply_text(reply)

@app.on_message(filters.command("play") & filters.group)
async def play_handler(client, message: Message):
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply_text("❌ Please provide a song name.")
    await play_music(client, message, pytgcalls, query)


@pytgcalls.on_stream_end()
async def stream_end_handler(client: PyTgCalls, update: Update):
    chat_id = update.chat_id
    await client.leave_group_call(chat_id)


if __name__ == "__main__":
    pytgcalls.start()
    app.run()
