from pyrogram import Client
from pyrogram.types import ChatMember
from typing import List

admin_cache = {}

async def get_admins(chat_id: int, client: Client) -> List[int]:
    if chat_id in admin_cache:
        return admin_cache[chat_id]

    admins = []
    async for member in client.get_chat_members(chat_id, filter="administrators"):
        admins.append(member.user.id)

    admin_cache[chat_id] = admins
    return admins
