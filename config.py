# config.py

import os
from dotenv import load_dotenv

# लोकल डेवलपमेंट के लिए .env फाइल से पढ़ने हेतु
load_dotenv()

# Telegram API credentials
# Koyeb पर ENV में API_ID और API_HASH सेट करें
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")

# Bot token: BotFather से मिला token
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# MongoDB URI: 여러 이름ों से fallback लें
MONGO_URI = (
    os.getenv("MONGO_URI")
    or os.getenv("MONGO_DB_URI")
    or os.getenv("MONGO_URL")
    or ""
)

# Optional: Owner ID (यदि कहीं उपयोग हो)
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# Optional settings
DURATION_LIMIT = int(os.getenv("DURATION_LIMIT", "180"))
COMMAND_PREFIXES = list(os.getenv("COMMAND_PREFIXES", "/ ! .").split())

# Logging group ID: यदि Telegram में बॉट लॉग भेजना हो
# यदि नहीं चाहते, तो सेट न करें या 0 रखें
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))

# Bot display name
MUSIC_BOT_NAME = os.getenv("MUSIC_BOT_NAME", "Music AI Bot")

# Auto leaving assistant settings (यदि उपयोग हो)
AUTO_LEAVING_ASSISTANT = os.getenv("AUTO_LEAVING_ASSISTANT", "False").lower() == "true"
ASSISTANT_LEAVE_TIME = int(os.getenv("ASSISTANT_LEAVE_TIME", "5400"))

# Support channel/group links
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "")

# AI feature enabled by default?
# यदि g4f free proxy या simple AI इस्तेमाल कर रहे हों, तो यह flag control कर सकता है
AI_CHAT_ENABLED = os.getenv("AI_CHAT_ENABLED", "True").lower() == "true"

# (यदि OpenAI या Hugging Face API key उपयोग हों तो यहां पढ़ें; 
#  यदि g4f approach है तो API key की ज़रूरत नहीं)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
HF_API_TOKEN = os.getenv("HF_API_TOKEN", "")

# Timezone setting (optional) यदि 코드 में आवश्यकता हो
TIMEZONE = os.getenv("TZ", "Asia/Kolkata")

# Validate कि आवश्यक vars सेट हैं, warn print करें (optional)
def validate_config():
    missing = []
    if API_ID == 0 or not API_HASH:
        missing.append("API_ID/API_HASH")
    if not BOT_TOKEN:
        missing.append("BOT_TOKEN")
    if not MONGO_URI:
        missing.append("MONGO_URI")
    # OPENAI_API_KEY या HF_API_TOKEN optional, g4f use करते हैं तो skip
    if missing:
        print(f"[WARNING] Missing required config vars: {', '.join(missing)}")

validate_config()
