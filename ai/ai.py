import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# G4F import
try:
    import g4f
    from g4f.client import Client
except ImportError:
    g4f = None

# 🌟 Fallback message with buttons
def fallback_message():
    return (
        "⚠️ अभी AI जवाब देने में दिक्कत आ रही है।\n\n"
        "🔁 कृपया थोड़ी देर बाद फिर कोशिश करें।\n\n"
        "👇 तब तक हमारे चैनल और ग्रुप से जुड़ें:",
        InlineKeyboardMarkup([
            [InlineKeyboardButton("🎬 Movie Group", url="https://t.me/iStreamX")],
            [InlineKeyboardButton("📢 Update Channel", url="https://t.me/asbhai_bsr")]
        ])
    )

# ✅ Free AI जवाब देने वाला function
async def generate_ai_reply(user_message):
    if g4f:
        try:
            client = Client()
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}],
            )
            return response.choices[0].message.content, None
        except Exception as e:
            print("❌ G4F error:", e)

    # fallback message अगर AI फेल हो जाए
    return fallback_message()
