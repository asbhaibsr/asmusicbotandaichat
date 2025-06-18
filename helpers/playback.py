import os
import youtube_dl
from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream, AudioPiped


ydl_opts = {
    'format': 'bestaudio/best',
    'quiet': True,
    'geo_bypass': True,
    'nocheckcertificate': True,
    'noplaylist': True,
    'extract_flat': False,
    'forceipv4': True,
}


async def play_music(client: Client, chat_id: int, query: str):
    """Play music in group call."""
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        url = info['url']
        title = info.get('title', 'Music')

    stream = AudioPiped(url)
    
    await client.send_message(chat_id, f"🎵 Playing: **{title}**")
    await client.pytgcalls.join_group_call(
        chat_id,
        InputStream(stream),
        stream_type="local_stream"
    )
