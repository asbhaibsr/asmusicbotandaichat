import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls import PyTgCallsClient # <--- यहाँ फिर से बदला है
from motor.motor_asyncio import AsyncIOMotorClient
from config import API_ID, API_HASH, BOT_TOKEN, MONGO_URI
from pyrogram import idle
from helpers.clean import auto_clean
from ai import generate_ai_reply

# 🎵 Music command handlers
from commands.play import play_handler
from commands.pause import pause_handler
from commands.resume import resume_handler
from commands.leave import leave_handler
from commands.stop import stop_handler

# Bot client
app = Client("MusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCallsClient(app) # यह लाइन सही है

# MongoDB setup
db = AsyncIOMotorClient(MONGO_URI).botdb
chatdb = db.chatmode

# /start command (private chat)
@app.on_message(filters.command("start") & filters.private)
async def start_msg(_, message: Message):
    buttons = [
        [InlineKeyboardButton("🎧 Add Me to Group", url=f"https://t.me/{app.me.username}?startgroup=true")],
        [InlineKeyboardButton("📢 Update Channel", url="https://t.me/asbhai_bsr"),
         InlineKeyboardButton("🎬 Movie Group", url="https://t.me/iStreamX")]
    ]
    await message.reply_text(
        "🌸 𝗛𝗲𝗹𝗹𝗼! 𝗠𝗲𝗶𝗻 𝗘𝗸 𝗙𝘂𝗹𝗹 𝗙𝗲𝗮𝘁𝘂𝗿𝗲 𝗠𝘂𝘀𝗶𝗰 + 𝗔𝗜 𝗚𝗶𝗿𝗹 𝗕𝗼𝘁 𝗛𝘂𝗻 💖\n\n"
        "🎶 Use /play <song name> in groups.\n"
        "🧠 Use /ai_on or /ai_off to toggle AI Chat in group.\n\n"
        "🔗 Movie Group: @iStreamX\n📢 Updates: @asbhai_bsr",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# AI on/off
@app.on_message(filters.command("ai_on") & filters.group)
async def enable_ai(_, message: Message):
    await chatdb.update_one({"chat_id": message.chat.id}, {"$set": {"ai": True}}, upsert=True)
    await message.reply_text("✅ AI Chat Enabled in this group!")

@app.on_message(filters.command("ai_off") & filters.group)
async def disable_ai(_, message: Message):
    await chatdb.update_one({"chat_id": message.chat.id}, {"$set": {"ai": False}}, upsert=True)
    await message.reply_text("❌ AI Chat Disabled in this group.")

# Group AI reply
@app.on_message(filters.text & filters.group & ~filters.command(["ai_on", "ai_off", "play"]))
async def group_ai_reply(_, message: Message):
    data = await chatdb.find_one({"chat_id": message.chat.id})
    if data and data.get("ai") is True:
        if message.text.startswith("/"):
            return
        reply = await generate_ai_reply(message.text)

        # Fallback message check
        if isinstance(reply, tuple):
            text, markup = reply
            await message.reply_text(text, reply_markup=markup)
        else:
            await message.reply_text(reply)

# Music Commands
@app.on_message(filters.command("play") & filters.group)
async def play_command(_, message: Message):
    await play_handler(pytgcalls, message)

@app.on_message(filters.command("pause") & filters.group)
async def pause_command(_, message: Message):
    await pause_handler(pytgcalls, message)

@app.on_message(filters.command("resume") & filters.group)
async def resume_command(_, message: Message):
    await resume_handler(pytgcalls, message)

@app.on_message(filters.command("stop") & filters.group)
async def stop_command(_, message: Message):
    await stop_handler(pytgcalls, message)

@app.on_message(filters.command("leave") & filters.group)
async def leave_command(_, message: Message):
    await leave_handler(pytgcalls, message)

# Main start
async def main():
    await app.start()
    await pytgcalls.start()
    asyncio.create_task(auto_clean())
    print("✅ Bot is Live with AI + Music!")
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
