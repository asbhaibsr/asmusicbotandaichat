from pyrogram import Client, filters
from pyrogram.types import Message
from config import AI_CHAT_ENABLED


@Client.on_message(filters.command("ai on") & filters.group)
async def ai_on(client, message: Message):
    chat_id = message.chat.id
    AI_CHAT_ENABLED[chat_id] = True
    await message.reply("🤖 AI Chat has been **enabled** for this group!")

    
@Client.on_message(filters.command("ai off") & filters.group)
async def ai_off(client, message: Message):
    chat_id = message.chat.id
    AI_CHAT_ENABLED[chat_id] = False
    await message.reply("🚫 AI Chat has been **disabled** for this group!")
