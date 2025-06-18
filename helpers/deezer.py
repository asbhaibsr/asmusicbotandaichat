import aiohttp


async def search_deezer(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.deezer.com/search?q={query}") as resp:
            if resp.status != 200:
                return None
            data = await resp.json()
            if data["data"]:
                return {
                    "title": data["data"][0]["title"],
                    "artist": data["data"][0]["artist"]["name"],
                    "duration": data["data"][0]["duration"],
                    "link": data["data"][0]["link"],
                    "thumbnail": data["data"][0]["album"]["cover_big"],
                }
            return None
