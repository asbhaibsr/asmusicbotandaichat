import asyncio
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.stream import StreamAudioEnded
from pyrogram import Client
from pyrogram.types import Message
from helpers.ytdl import get_yt_info
from pytgcalls.types.input_stream import AudioPiped

active_chats = {}

async def stream_music(client: Client, pytgcalls: PyTgCalls, message: Message, query: str):
    chat_id = message.chat.id
    info = get_yt_info(query)
    if not info:
        return await message.reply_text("❌ Song not found!")

    url = info["url"]
    title = info["title"]
    duration = info["duration"]

    await message.reply_text(f"🎵 Playing: {title} ({duration} sec)")

    await pytgcalls.join_group_call(
        chat_id,
        AudioPiped(url),
        stream_type=InputAudioStream,
    )

    active_chats[chat_id] = {
        "title": title,
        "duration": duration,
        "url": url
    }

    # Wait for song end
    await asyncio.sleep(duration)
    await pytgcalls.leave_group_call(chat_id)
    active_chats.pop(chat_id, None)

@PyTgCalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: StreamAudioEnded):
    chat_id = update.chat_id
    await client.leave_group_call(chat_id)
    active_chats.pop(chat_id, None)
