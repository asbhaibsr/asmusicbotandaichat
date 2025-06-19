import asyncio
from pyrogram.errors import FloodWait

async def auto_clean():
    while True:
        await asyncio.sleep(3600)  # हर 1 घंटे में clean
        try:
            # Future scope: Add cleaning logic here if needed
            pass
        except FloodWait as e:
            await asyncio.sleep(e.value)
