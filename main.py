import asyncio
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram.types import Message
from pytgcalls import PyTgCalls

app = Client("MusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(app)

# MongoDB setup
db = AsyncIOMotorClient(os.environ.get("MONGO_URI")).botdb
chatdb = db.chatmode

# Start-up event
@app.on_message(filters.command("start") & filters.private)
async def start_msg(_, message: Message):
    await message.reply_text("🌸 Hello! I'm your Yukki-style Music + AI Chat Bot.\nUse /ai_on or /ai_off to toggle AI Chat.\nUse /play <song> in groups.")

# AI toggle ON
@app.on_message(filters.command("ai_on") & filters.group)
async def ai_on(_, message: Message):
    await chatdb.update_one({"chat_id": message.chat.id}, {"$set": {"ai": True}}, upsert=True)
    await message.reply_text("🤖 AI Chat Enabled in this group!")

# AI toggle OFF
@app.on_message(filters.command("ai_off") & filters.group)
async def ai_off(_, message: Message):
    await chatdb.update_one({"chat_id": message.chat.id}, {"$set": {"ai": False}}, upsert=True)
    await message.reply_text("🔇 AI Chat Disabled in this group.")

# AI Reply Handler (only if enabled)
@app.on_message(filters.text & filters.group)
async def ai_reply(_, message: Message):
    data = await chatdb.find_one({"chat_id": message.chat.id})
    if data and data.get("ai") is True:
        if message.text.startswith("/"):
            return  # skip commands
        reply = f"💬 (AI): Tumne kaha: {message.text}"  # Replace with real AI logic
        await message.reply_text(reply)

# Play music (stub)
@app.on_message(filters.command("play") & filters.group)
async def play_music(_, message: Message):
    await message.reply_text("🎵 Playing music feature will be handled here (add logic).")

async def main():
    await app.start()
    await pytgcalls.start()
    print("🤖 Bot is running...")
    await idle()
    await app.stop()

if __name__ == "__main__":
    from pyrogram import idle
    asyncio.run(main())
