import yt_dlp
import os

YDL_OPTIONS = {
    'format': 'bestaudio',
    'noplaylist': True,
    'quiet': True,
    'extract_flat': False,
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


async def download_audio(query: str):
    try:
        with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
            title = info.get("title", None)
            duration = info.get("duration", None)

            # Ab download kare
            ydl.download([info['webpage_url']])
            filename = ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3")

        return {
            "title": title,
            "duration": duration,
            "filepath": filename
        }

    except Exception as e:
        print(f"[ERROR] in ytdl.py: {e}")
        return None
