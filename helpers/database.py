import motor.motor_asyncio
from os import getenv

MONGO_URL = getenv("MONGO_URL", None)

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client["as_music_ai_bot"]  # You can rename this

users = db.users
chats = db.chats
settings = db.settings


async def add_user(user_id: int):
    user = await users.find_one({"_id": user_id})
    if not user:
        await users.insert_one({"_id": user_id})


async def is_user(user_id: int):
    return await users.find_one({"_id": user_id})


async def add_chat(chat_id: int):
    chat = await chats.find_one({"_id": chat_id})
    if not chat:
        await chats.insert_one({"_id": chat_id})


async def is_chat(chat_id: int):
    return await chats.find_one({"_id": chat_id})


async def total_users():
    return await users.count_documents({})


async def total_chats():
    return await chats.count_documents({})


async def set_ai_toggle(chat_id: int, status: bool):
    await settings.update_one(
        {"_id": chat_id}, {"$set": {"ai_enabled": status}}, upsert=True
    )


async def is_ai_enabled(chat_id: int):
    doc = await settings.find_one({"_id": chat_id})
    return doc.get("ai_enabled", False) if doc else False
