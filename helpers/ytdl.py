import yt_dlp

ydl_opts = {
    "format": "bestaudio[ext=m4a]",
    "noplaylist": True,
    "quiet": True,
    "extract_flat": "in_playlist",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "default_search": "ytsearch",
    "skip_download": True,
}

def get_yt_info(query: str):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(query, download=False)
            if "entries" in info:
                info = info["entries"][0]
            return {
                "title": info.get("title"),
                "url": info.get("webpage_url"),
                "duration": info.get("duration"),
                "id": info.get("id"),
            }
        except Exception as e:
            print(f"❌ YT-DLP Error: {e}")
            return None
