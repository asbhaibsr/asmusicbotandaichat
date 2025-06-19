# bot.py

from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, SESSION_STRING, OWNER_ID
from ai import generate_ai_reply
from music.handlers import play  # this auto-loads play commands
import asyncio

# Client Setup
app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

pytgcalls = PyTgCalls(app)

# Dict to toggle AI per group
ai_enabled = {}

# /start command
@app.on_message(filters.command("start") & filters.private)
async def start_private(_, message: Message):
    await message.reply_text(
        "**Hey Jaanu 😘,**\n\n"
        "Main ek intelligent girl bot hoon 💋\n"
        "🎶 Songs bhi chala sakti hoon aur 🧠 baatein bhi kar sakti hoon.\n\n"
        "**Commands:**\n"
        "`/play [song name or reply]` - song chalane ke liye\n"
        "`/ai on` - AI chat chalu kare\n"
        "`/ai off` - AI band kare"
    )

# AI toggle on/off
@app.on_message(filters.command("ai") & filters.group)
async def toggle_ai(_, message: Message):
    chat_id = message.chat.id
    cmd = message.command

    if len(cmd) < 2:
        return await message.reply("🧠 Use `/ai on` ya `/ai off`")

    if cmd[1] == "on":
        ai_enabled[chat_id] = True
        await message.reply("✅ AI chat chalu kar diya gaya!")
    elif cmd[1] == "off":
        ai_enabled[chat_id] = False
        await message.reply("❌ AI chat band kar diya gaya!")
    else:
        await message.reply("⚠️ Galat command! Use `/ai on` ya `/ai off`")

# AI Reply handler
@app.on_message(filters.text & filters.group & ~filters.command(["play", "skip", "stop"]))
async def group_ai(_, message: Message):
    chat_id = message.chat.id

    if ai_enabled.get(chat_id):
        await message.reply_chat_action("typing")
        reply = await generate_ai_reply(message.from_user.id, message.text)
        await message.reply_text(reply)

# Main
async def main():
    await app.start()
    await pytgcalls.start()
    print("🤖 Bot chalu ho gaya!")
    await asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    asyncio.run(main())
