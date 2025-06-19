from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.input_stream.input_file import InputAudioStream
from yt_dlp import YoutubeDL
import os

# Download audio from YouTube
def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(id)s.%(ext)s',
        'quiet': True,
        'noplaylist': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

# Stream the audio
async def stream_audio(pytgcalls: PyTgCalls, chat_id: int, url: str):
    file_path = download_audio(url)
    await pytgcalls.join_group_call(
        chat_id,
        InputStream(
            InputAudioStream(
                file_path,
                HighQualityAudio()
            )
        ),
        stream_type='local_stream'
    )
