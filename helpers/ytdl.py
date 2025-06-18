# helpers/ytdl.py

from yt_dlp import YoutubeDL

YDL_OPTS = {
    "format": "bestaudio/best",
    "quiet": True,
    "geo_bypass": True,
    "nocheckcertificate": True,
    "ignoreerrors": True,
    "logtostderr": False,
    "source_address": "0.0.0.0"
}

def extract_info(url):
    try:
        with YoutubeDL(YDL_OPTS) as ytdl:
            info = ytdl.extract_info(url, download=False)
            return info
    except Exception as e:
        print(f"YT-DLP Error: {e}")
        return None
