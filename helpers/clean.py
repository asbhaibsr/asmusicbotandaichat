import asyncio
import os

# Clean downloaded files every 10 mins
async def auto_clean():
    while True:
        try:
            for file in os.listdir("downloads"):
                if file.endswith(".webm") or file.endswith(".m4a") or file.endswith(".mp3"):
                    os.remove(os.path.join("downloads", file))
        except Exception as e:
            print("Cleanup Error:", e)
        await asyncio.sleep(600)  # wait 10 minutes
