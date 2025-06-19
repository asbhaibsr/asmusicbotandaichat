from pyrogram.types import Message

async def resume_handler(pytgcalls, message: Message):
    try:
        await pytgcalls.resume_stream(message.chat.id)
        await message.reply_text("▶️ Music resumed.")
    except Exception as e:
        await message.reply_text(f"❌ Error resuming music: {e}")
