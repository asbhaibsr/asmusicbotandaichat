import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "29970536"))
API_HASH = os.getenv("API_HASH", "f4bfdcdd4a5c1b7328a7e4f25f024a09")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

OWNER_ID = int(os.getenv("OWNER_ID", "7315805581"))

DURATION_LIMIT = int(os.getenv("DURATION_LIMIT", "180"))
COMMAND_PREFIXES = list(os.getenv("COMMAND_PREFIXES", "/ ! .").split())

LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-100"))
MUSIC_BOT_NAME = os.getenv("MUSIC_BOT_NAME", "💖 AsMusic AI Bot")

AUTO_LEAVING_ASSISTANT = os.getenv("AUTO_LEAVING_ASSISTANT", "False").lower() == "true"
ASSISTANT_LEAVE_TIME = int(os.getenv("ASSISTANT_LEAVE_TIME", "5400"))

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/asbhai_bsr")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/iStreamX")

AI_CHAT_ENABLED = os.getenv("AI_CHAT_ENABLED", "True").lower() == "true"
