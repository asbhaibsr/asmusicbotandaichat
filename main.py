import os
import asyncio
from threading import Thread
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from motor.motor_asyncio import AsyncIOMotorClient
from config import API_ID, API_HASH, BOT_TOKEN, MONGO_URI
from helpers.clean import auto_clean  # आपका existing clean मॉड्यूल
from keep_alive import keep_alive

# ---------------------------------------------------
# 1) Flask keep-alive सर्वर को बैकग्राउंड थ्रेड में स्टार्ट करें
# ---------------------------------------------------
Thread(target=keep_alive, daemon=True).start()

# ---------------------------------------------------
# 2) Pyrogram Bot Client और PyTgCalls सेटअप
# ---------------------------------------------------
app = Client(
    "MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    # parse_mode="html"  # अगर HTML parse चाहते हैं तो uncomment करें
)
pytgcalls = PyTgCalls(app)

# ---------------------------------------------------
# 3) MongoDB Setup (chatmode collection में AI toggle स्टोर होगा)
# ---------------------------------------------------
db = AsyncIOMotorClient(MONGO_URI).botdb
chatdb = db.chatmode

# ---------------------------------------------------
# 4) Command Handlers
# ---------------------------------------------------

# /start in private chat
@app.on_message(filters.command("start") & filters.private)
async def start_msg(_, message: Message):
    await message.reply_text(
        "🌸 Hello! I'm your Yukki-style Music + AI Chat Bot.\n\n"
        "🎶 Use /play <song name> in groups.\n"
        "🧠 Use /ai_on or /ai_off to toggle AI Chat in group.\n\n"
        "🔗 Movie Group: @iStreamX\n📢 Updates: @asbhai_bsr"
    )

# /ai_on in group
@app.on_message(filters.command("ai_on") & filters.group)
async def ai_on(_, message: Message):
    await chatdb.update_one(
        {"chat_id": message.chat.id},
        {"$set": {"ai": True}},
        upsert=True
    )
    await message.reply_text("🤖 AI Chat Enabled in this group!")

# /ai_off in group
@app.on_message(filters.command("ai_off") & filters.group)
async def ai_off(_, message: Message):
    await chatdb.update_one(
        {"chat_id": message.chat.id},
        {"$set": {"ai": False}},
        upsert=True
    )
    await message.reply_text("🔇 AI Chat Disabled in this group.")

# AI Chat handler: केवल तब जब AI ON हो
@app.on_message(filters.text & filters.group)
async def ai_reply(_, message: Message):
    data = await chatdb.find_one({"chat_id": message.chat.id})
    if data and data.get("ai") is True:
        if message.text.startswith("/"):
            return
        # यहाँ आप असली AI लॉजिक लगा सकते हैं
        reply = f"💬 (AI): Tumne kaha: {message.text}"
        await message.reply_text(reply)

# /play placeholder (आप यहाँ music logic जोड़ें)
@app.on_message(filters.command("play") & filters.group)
async def play_music(_, message: Message):
    await message.reply_text("🎧 Playing music feature will be handled here soon!")

# ---------------------------------------------------
# 5) Main Start Function
# ---------------------------------------------------
async def run():
    # Bot start
    await app.start()
    # PyTgCalls start (अगर music जोड़ रहे हैं)
    try:
        await pytgcalls.start()
    except Exception as e:
        # अगर PyTgCalls कॉन्फ़िगरेशन में error आए तो लॉग कर सकते हैं
        print(f"[WARN] PyTgCalls start error: {e}")
    # auto_clean task (यदि helpers.clean.auto_clean मौजूद है)
    try:
        asyncio.create_task(auto_clean())
    except Exception as e:
        print(f"[WARN] auto_clean task error: {e}")

    print("🤖 Bot is running with AI + Music!")
    # Idle रखे जब तक manual stop या instance stop न हो
    await idle()
    # Cleanup on stop (यहाँ पर optional; Koyeb instance बंद होते समय बॉट को ठीक से बंद करेगा)
    await app.stop()

if __name__ == "__main__":
    # asyncio.run(run())  # आम तौर पर यही चलेगा
    # कभी-कभी nested loop issue हो तो alternate रख सकते हैं:
    try:
        asyncio.get_event_loop().run_until_complete(run())
    except RuntimeError:
        asyncio.run(run())
