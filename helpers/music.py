from pytgcalls.types.input_stream import InputStream, AudioPiped
import yt_dlp

class MusicPlayer:
    def __init__(self, call, queue_col):
        self.call = call
        self.queue_col = queue_col
        self.active = {}

    async def play_song(self, chat_id, query, msg):
        await msg.reply(f"🎵 Playing: {query}")
        ydl = yt_dlp.YoutubeDL({'format': 'bestaudio', 'noplaylist': True})
        info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        url = info['url']
        await self.call.join_group_call(
            chat_id,
            InputStream(AudioPiped(url))
        )
        self.active[chat_id] = url

    async def pause(self, chat_id, msg):
        await self.call.pause_stream(chat_id)
        await msg.reply("⏸️ Paused.")

    async def stop(self, chat_id, msg):
        await self.call.leave_group_call(chat_id)
        await msg.reply("⏹️ Stopped.")
