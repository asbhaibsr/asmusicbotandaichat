from youtubesearchpython import VideosSearch


async def get_youtube_url(query: str):
    try:
        videosSearch = VideosSearch(query, limit=1)
        result = (await videosSearch.next())['result']
        if not result:
            return None
        return result[0]['link']
    except Exception as e:
        print(f"[YouTube Search Error] {e}")
        return None
