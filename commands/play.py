from pytgcalls.types.stream import StreamAudioEnded
from pytgcalls.types.input_stream import InputAudioStream
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream.input_audio import AudioPiped
import asyncio

async def play_handler(pytgcalls: PyTgCalls, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("🔍 Please provide a song name to play!")

    song_name = " ".join(message.command[1:])
    await message.reply_text(f"🎶 Playing: {song_name} (Demo Mode)")

    await pytgcalls.join_group_call(
        message.chat.id,
        AudioPiped("https://file-examples.com/storage/fe79c1537e7b90b3c5f95ae/2017/11/file_example_MP3_700KB.mp3")
    )
