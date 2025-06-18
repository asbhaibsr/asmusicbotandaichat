import asyncio
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream.input_audio import InputAudioStream
from pytgcalls.types.input_stream.input_video import InputVideoStream

from config import API_ID, API_HASH, BOT_TOKEN
from pyrogram import Client
from yt_dlp import YoutubeDL

app = Client("MusicAssistant", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(app)

ydl_opts = {
    "format": "bestaudio/best",
    "quiet": True,
    "geo_bypass": True,
    "nocheckcertificate": True,
    "noplaylist": True,
    "extract_flat": False,
    "forceipv4": True,
}

video_opts = {
    "format": "best[ext=mp4]",
    "quiet": True,
    "geo_bypass": True,
    "nocheckcertificate": True,
    "noplaylist": True,
    "extract_flat": False,
    "forceipv4": True,
}


async def stream_audio(client, message, query, title=None):
    await message.reply("🔍 Searching...")
    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(query, download=False)
            url = info['url']
        except Exception as e:
            return await message.reply(f"❌ Failed to fetch audio: {e}")
    
    chat_id = message.chat.id
    try:
        await pytgcalls.join_group_call(
            chat_id,
            InputStream(InputAudioStream(url)),
            stream_type="local_stream"
        )
        await message.reply(f"▶️ Playing **{title or query}**")
    except Exception as e:
        await message.reply(f"❌ Error: {e}")


async def stream_video(client, message, query):
    await message.reply("📺 Fetching video...")
    with YoutubeDL(video_opts) as ydl:
        try:
            info = ydl.extract_info(query, download=False)
            url = info['url']
            title = info.get('title', 'Video')
        except Exception as e:
            return await message.reply(f"❌ Video fetch error: {e}")
    
    chat_id = message.chat.id
    try:
        await pytgcalls.join_group_call(
            chat_id,
            InputStream(InputVideoStream(url)),
            stream_type="local_stream"
        )
        await message.reply(f"▶️ Streaming Video: **{title}**")
    except Exception as e:
        await message.reply(f"❌ Stream error: {e}")


@app.on_message()
async def init_pytgcalls(_, __):
    pass


async def start_call():
    await app.start()
    await pytgcalls.start()
    print("✅ Music Streaming Bot Ready!")
    await idle()
