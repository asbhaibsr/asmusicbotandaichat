import g4f
import asyncio

# MAIN FUNCTION
async def generate_ai_reply(message: str) -> str:
    try:
        reply = await gpt_g4f(message)
        return reply
    except Exception:
        return ai_failed_message()

# g4f (Free AI)
async def gpt_g4f(prompt):
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_35_turbo,
        messages=[{"role": "user", "content": prompt}]
    )
    return response

# Agar g4f bhi fail ho jaaye to fallback message
def ai_failed_message():
    return "🤖 AI अभी जवाब नहीं दे पा रहा!\n\n👇 नीचे से हमारे चैनल और मूवी ग्रुप जॉइन करें:\n📢 @asbhai_bsr\n🎬 @iStreamX"
