import yt_dlp

YDL_OPTS = {
    "format": "bestaudio/best",
    "noplaylist": True,
    "quiet": True,
    "outtmpl": "downloads/%(title)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}


async def extract_info(query: str):
    try:
        with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)["entries"][0]
            return {
                "title": info["title"],
                "url": info["webpage_url"],
                "filepath": ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3"),
                "duration": info.get("duration")
            }
    except Exception as e:
        print(f"[YTDL ERROR] {e}")
        return None
