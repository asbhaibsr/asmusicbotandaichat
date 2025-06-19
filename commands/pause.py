from pyrogram.types import Message

async def pause_handler(pytgcalls, message: Message):
    try:
        await pytgcalls.pause_stream(message.chat.id)
        await message.reply_text("⏸️ Music paused.")
    except Exception as e:
        await message.reply_text(f"❌ Error pausing music: {e}")
