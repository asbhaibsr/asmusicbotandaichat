from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message: Message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/15d6897cc012dfea3a390.jpg",
        caption=f"💖 𝐇𝐞𝐲 {message.from_user.mention}!\n\n"
                "𝘔𝘢𝘪𝘯 𝘦𝘬 𝘈𝘐 + 𝘔𝘶𝘴𝘪𝘤 𝘉𝘰𝘵 𝘩𝘶!\n"
                "➤ 𝘎𝘳𝘰𝘶𝘱 𝘮𝘦𝘪𝘯 𝘔𝘶𝘴𝘪𝘤 𝘤𝘩𝘢𝘭𝘢𝘢𝘯𝘢 𝘢𝘶𝘳 𝘗𝘳𝘪𝘷𝘢𝘵𝘦 𝘮𝘦𝘪𝘯 𝘣𝘢𝘢𝘵𝘤𝘩𝘦𝘦𝘵 𝘬𝘢𝘳𝘯𝘢 𝘮𝘦𝘳𝘢 𝘤𝘩𝘢𝘮𝘢𝘵𝘬𝘢𝘳 𝘩𝘢𝘪 😍",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ➕", url=f"https://t.me/{client.me.username}?startgroup=true")],
            [InlineKeyboardButton("🎬 Movie Group", url="https://t.me/iStreamX"),
             InlineKeyboardButton("📢 Updates", url="https://t.me/asbhai_bsr")]
        ])
    )
