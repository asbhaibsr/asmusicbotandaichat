from pyrogram.types import Message

async def leave_handler(pytgcalls, message: Message):
    try:
        await pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("👋 Left the voice chat.")
    except Exception as e:
        await message.reply_text(f"❌ Error leaving VC: {e}")
