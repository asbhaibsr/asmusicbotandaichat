import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from motor.motor_asyncio import AsyncIOMotorClient
from config import API_ID, API_HASH, BOT_TOKEN, MONGO_URI
from helpers.clean import auto_clean
from pyrogram import idle

# 👇 Keep-alive for Koyeb Health Check
from keep_alive import keep_alive
keep_alive()

# Pyrogram Bot Client
app = Client("MusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(app)

# MongoDB Setup
db = AsyncIOMotorClient(MONGO_URI).botdb
chatdb = db.chatmode

# /start in PM
@app.on_message(filters.command("start") & filters.private)
async def start_msg(_, message: Message):
    await message.reply_text(
        "🌸 Hello! I'm your Yukki-style Music + AI Chat Bot.\n\n"
        "🎶 Use /play <song name> in groups.\n"
        "🧠 Use /ai_on or /ai_off to toggle AI Chat in group.\n\n"
        "🔗 Movie Group: @iStreamX\n📢 Updates: @asbhai_bsr"
    )

# Enable AI in group
@app.on_message(filters.command("ai_on") & filters.group)
async def ai_on(_, message: Message):
    await chatdb.update_one({"chat_id": message.chat.id}, {"$set": {"ai": True}}, upsert=True)
    await message.reply_text("🤖 AI Chat Enabled in this group!")

# Disable AI in group
@app.on_message(filters.command("ai_off") & filters.group)
async def ai_off(_, message: Message):
    await chatdb.update_one({"chat_id": message.chat.id}, {"$set": {"ai": False}}, upsert=True)
    await message.reply_text("🔇 AI Chat Disabled in this group.")

# AI Chat Response
@app.on_message(filters.text & filters.group)
async def ai_reply(_, message: Message):
    data = await chatdb.find_one({"chat_id": message.chat.id})
    if data and data.get("ai") is True:
        if message.text.startswith("/"):
            return
        try:
            from ai_reply import generate_ai_reply
            reply = await generate_ai_reply(message.text)
        except Exception as e:
            reply = f"💬 (AI): Tumne kaha: {message.text}\n(AI error: {e})"
        await message.reply_text(reply)

# /play command (placeholder)
@app.on_message(filters.command("play") & filters.group)
async def play_music(_, message: Message):
    await message.reply_text("🎧 Playing music feature will be handled here soon!")

# Main Start Function
async def main():
    await app.start()
    await pytgcalls.start()
    asyncio.create_task(auto_clean())  # Start auto clean
    print("🤖 Bot is running with AI + Music!")
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
