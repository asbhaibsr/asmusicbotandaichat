from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID, AI_USERS
from utils.ai_reply import get_ai_reply

# Toggle AI chat: /ai on or /ai off
@Client.on_message(filters.command("ai") & filters.user(OWNER_ID))
async def toggle_ai(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("✅ Use `/ai on` or `/ai off`")
    
    arg = message.command[1].lower()
    if arg == "on":
        AI_USERS.add(message.chat.id)
        await message.reply("🤖 AI chat enabled!")
    elif arg == "off":
        AI_USERS.discard(message.chat.id)
        await message.reply("🚫 AI chat disabled!")
    else:
        await message.reply("❌ Unknown command. Use `/ai on` or `/ai off`")

# Handle private AI chat messages
@Client.
