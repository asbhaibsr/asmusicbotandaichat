import yt_dlp

def get_yt_info(query):
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "noplaylist": True,
            "quiet": True,
            "extract_flat": "in_playlist",
            "default_search": "ytsearch",
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            if "entries" in info:
                info = info["entries"][0]
            return {
                "url": info["url"],
                "title": info["title"],
                "duration": int(info["duration"]),
            }
    except Exception as e:
        print(f"[❌] yt-dlp error: {e}")
        return None
