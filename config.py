import os
from dotenv import load_dotenv

# लोकल dev में .env से लोड करने के लिए (Koyeb में ये नहीं पढ़ता लेकिन local dev में काम आएगा)
load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))        # Koyeb में सेट होना चाहिए
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
# MONGO_URI fetch करें (fallback कुछ नामों से)
MONGO_URI = (
    os.getenv("MONGO_URI")
    or os.getenv("MONGO_DB_URI")
    or os.getenv("MONGO_URL")
    or ""
)

OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# Optional settings; अगर नहीं चाहिए तो default रखें
DURATION_LIMIT = int(os.getenv("DURATION_LIMIT", "180"))
COMMAND_PREFIXES = list(os.getenv("COMMAND_PREFIXES", "/ ! .").split())
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))  # अगर logging group नहीं चाहिए तो 0 या None handle करें
MUSIC_BOT_NAME = os.getenv("MUSIC_BOT_NAME", "AsMusic AI Bot")

AUTO_LEAVING_ASSISTANT = os.getenv("AUTO_LEAVING_ASSISTANT", "False").lower() == "true"
ASSISTANT_LEAVE_TIME = int(os.getenv("ASSISTANT_LEAVE_TIME", "5400"))

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "")
AI_CHAT_ENABLED = os.getenv("AI_CHAT_ENABLED", "True").lower() == "true"
