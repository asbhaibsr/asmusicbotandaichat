from pyrogram.types import Message

async def stop_handler(pytgcalls, message: Message):
    try:
        await pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("⏹️ Music stopped.")
    except Exception as e:
        await message.reply_text(f"❌ Error stopping: {e}")
