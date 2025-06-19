import random

# Try all free AI modules in order of reliability
try:
    from g4f.client import Client as G4FClient
except:
    G4FClient = None

try:
    import phind
except:
    phind = None

try:
    from yqcloud import ChatBot as YQCloudBot
except:
    YQCloudBot = None

try:
    from gemini import ChatBot as GeminiBot
except:
    GeminiBot = None

async def generate_ai_reply(user_message: str) -> str:
    # 1. Try G4F
    if G4FClient:
        try:
            client = G4FClient()
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}]
            )
            return response.choices[0].message.content.strip()
        except Exception:
            pass

    # 2. Try Phind
    if phind:
        try:
            return phind.chat(user_message)
        except Exception:
            pass

    # 3. Try YQCloud
    if YQCloudBot:
        try:
            bot = YQCloudBot(api_key="free")
            return await bot.chat(user_message)
        except Exception:
            pass

    # 4. Try Gemini
    if GeminiBot:
        try:
            bot = GeminiBot()
            return await bot.chat(user_message)
        except Exception:
            pass

    # Fallback message
    return "😔 Maaf karo, abhi main reply nahi de pa rahi hoon. Thodi der baad try karo!"

