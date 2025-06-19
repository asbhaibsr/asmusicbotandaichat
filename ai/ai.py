# ai.py
import random
import httpx
from pymongo import MongoClient
from config import MONGO_URI
from g4f.client import Client as G4FClient
from g4f.Provider import Phind, Yqcloud

# MongoDB setup
mongo_client = MongoClient(MONGO_URI)
db = mongo_client['ai_chat']
collection = db['user_messages']

# Fallback AI logic
async def generate_ai_reply(user_id, user_message):
    # Save message to DB
    collection.insert_one({
        "user_id": user_id,
        "message": user_message
    })

    # Try G4F with fallback providers
    try:
        g4f_client = G4FClient()
        completion = g4f_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            provider=random.choice([Phind, Yqcloud])
        )
        return completion.choices[0].message.content

    except Exception as e:
        print(f"[G4F Error] {e}")

    # Fallback 2: yqcloud API (Free)
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://yqcloud-openai.hf.space/api/gen",
                json={"text": user_message},
                timeout=30
            )
            if response.status_code == 200:
                return response.json().get("text", "No reply.")
    except Exception as e:
        print(f"[yqcloud error] {e}")

    # Fallback failed
    return "😓 Maaf karna jaanu, abhi jawab nahi de pa rahi hoon...\n\n🔁 <b>Try again later</b> ya <a href='https://t.me/asbhai_bsr'>Update Channel</a> check karo ❤️"
