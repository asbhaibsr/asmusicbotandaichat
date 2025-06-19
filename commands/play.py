from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream.input_url import AudioPiped
from youtubesearchpython import VideosSearch

async def play_handler(_, message: Message, app, pytgcalls: PyTgCalls):
    if len(message.command) < 2:
        return await message.reply("❗ Please provide a song name.")

    query = " ".join(message.command[1:])
    await message.reply("🔎 Searching on YouTube...")
    try:
        search = VideosSearch(query, limit=1)
        result = search.result()["result"][0]
        url = result["link"]

        await pytgcalls.join_group_call(
            chat_id=message.chat.id,
            stream=AudioPiped(url),
            stream_type=InputStream().STREAM,
        )

        await message.reply(f"🎶 Playing: [{result['title']}]({url})", disable_web_page_preview=True)
    except Exception as e:
        await message.reply(f"❌ Failed to play song.\n**Error:** `{e}`")
