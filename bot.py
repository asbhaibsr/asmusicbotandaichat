import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
from ai import generate_ai_reply  # AI logic
from utils.music_stream import stream_audio, stream_video, start_call

from pyrogram.enums import ChatType

# Global AI toggle
ai_enabled = {}

app = Client("MusicAssistant", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        "👋 Hello! I'm your AI + Music Assistant.\n\n"
        "🎵 Use /play to play music\n"
        "💬 Talk to me if AI is ON\n"
        "🧠 Use /ai on or /ai off to toggle AI chat"
    )


@app.on_message(filters.command("ai"))
async def toggle_ai(client, message):
    if len(message.command) < 2:
        return await message.reply("🧠 Use `/ai on` or `/ai off`")

    chat_id = message.chat.id
    status = message.command[1].lower()

    if status == "on":
        ai_enabled[chat_id] = True
        await message.reply("✅ AI chat is now **enabled**.")
    elif status == "off":
        ai_enabled[chat_id] = False
        await message.reply("🛑 AI chat is now **disabled**.")
    else:
        await message.reply("⚠️ Unknown command! Use `/ai on` or `/ai off`")


@app.on_message(filters.command("play") & filters.group)
async def play_music(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: `/play song name`")
    query = " ".join(message.command[1:])
    await stream_audio(client, message, query)


@app.on_message(filters.command("vplay") & filters.group)
async def play_video(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: `/vplay video name`")
    query = " ".join(message.command[1:])
    await stream_video(client, message, query)


@app.on_message(filters.text & ~filters.command(["play", "vplay", "ai", "start"]))
async def ai_chat_handler(client, message: Message):
    if message.chat.type != ChatType.PRIVATE and not ai_enabled.get(message.chat.id):
        return  # Ignore if AI is off in group

    reply = await generate_ai_reply(message.text)
    await message.reply_text(reply)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_call())
