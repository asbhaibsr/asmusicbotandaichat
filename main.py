import os
import asyncio
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from motor.motor_asyncio import AsyncIOMotorClient
from config import API_ID, API_HASH, BOT_TOKEN, MONGO_URI
from helpers.clean import auto_clean
from keep_alive import keep_alive

# Flask server ko alag thread me run karo
keep_alive()

# Bot setup
app = Client("MusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(app)

# MongoDB setup
db = AsyncIOMotorClient(MONGO_URI).botdb
chatdb = db.chatmode

# START command
@app.on_message(filters.command("start") & filters.private)
async def start_msg(_, message: Message):
    await message.reply_text(
        "🌸 Hello! I'm your Yukki-style Music + AI Chat Bot.\n\n"
        "🎶 Use /play <song name> in groups.\n"
        "🧠 Use /ai_on or /ai_off to toggle AI Chat in group.\n\n"
        "🔗 Movie Group: @iStreamX\n📢 Updates: @asbhai_bsr"
    )

# AI ON
@app.on_message(filters.command("ai_on") & filters.group)
async def ai_on(_, message: Message):
    await chatdb.update_one({"chat_id": message.chat.id}, {"$set": {"ai": True}}, upsert=True)
    await message.reply_text("🤖 AI Chat Enabled in this group!")

# AI OFF
@app.on_message(filters.command("ai_off") & filters.group)
async def ai_off(_, message: Message):
    await chatdb.update_one({"chat_id": message.chat.id}, {"$set": {"ai": False}}, upsert=True)
    await message.reply_text("🔇 AI Chat Disabled in this group.")

# AI reply (dummy)
@app.on_message(filters.text & filters.group)
async def ai_reply(_, message: Message):
    data = await chatdb.find_one({"chat_id": message.chat.id})
    if data and data.get("ai") is True and not message.text.startswith("/"):
        await message.reply_text(f"💬 (AI): Tumne kaha: {message.text}")

# Music play (placeholder)
@app.on_message(filters.command("play") & filters.group)
async def play_music(_, message: Message):
    await message.reply_text("🎧 Playing music feature will be handled here soon!")

# MAIN function
async def main():
    await app.start()
    await pytgcalls.start()
    asyncio.create_task(auto_clean())
    print("🤖 Bot is running with AI + Music!")
    await idle()
    await app.stop()

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except:
        asyncio.run(main())
