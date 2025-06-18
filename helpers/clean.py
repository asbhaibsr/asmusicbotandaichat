# helpers/clean.py

import os
import asyncio

TEMP_DOWNLOAD_DIR = "downloads"

async def clean_downloads():
    try:
        for filename in os.listdir(TEMP_DOWNLOAD_DIR):
            file_path = os.path.join(TEMP_DOWNLOAD_DIR, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        return True
    except Exception as e:
        print(f"[Clean Error] {e}")
        return False

async def auto_clean(interval: int = 1800):
    while True:
        await clean_downloads()
        await asyncio.sleep(interval)
