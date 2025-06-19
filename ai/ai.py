import random
import g4f
import asyncio
import httpx
import google.generativeai as genai

# Google AI बिना key के काम नहीं करेगा, fallback में ही use होगा
try:
    genai.configure(api_key=None)  # FREE नहीं है, fallback handle किया है
except:
    pass

# MAIN FUNCTION
async def generate_ai_reply(message: str) -> str:
    try:
        reply = await gpt_g4f(message)
        return reply
    except Exception:
        try:
            reply = await gpt_gemini(message)
            return reply
        except Exception:
            return ai_failed_message()

# g4f (free backend)
async def gpt_g4f(prompt):
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_35_turbo,
        messages=[{"role": "user", "content": prompt}]
    )
    return response

# Google Gemini (API key नहीं होने पर भी fallback किया गया है)
async def gpt_gemini(prompt):
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text

# Agar dono fail ho jaaye to
def ai_failed_message():
    return "🤖 AI अभी busy है!\n\n👇 नीचे से हमारे चैनल और मूवी ग्रुप जॉइन करें:\n\n📢 @asbhai_bsr\n🎬 @iStreamX"
