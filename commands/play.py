from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped

async def play_handler(pytgcalls: PyTgCalls, message: Message):
    if not message.reply_to_message or not message.reply_to_message.audio:
        await message.reply_text("❌ कृपया किसी audio फाइल को reply करके /play भेजें।")
        return

    audio_file = await message.reply_to_message.download()
    await pytgcalls.join_group_call(
        message.chat.id,
        AudioPiped(audio_file)
    )
    await message.reply_text("🎶 गाना प्ले हो रहा है!")
