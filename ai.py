import random
import httpx

fallback_replies = [
    "Hmm, interesting... 💭",
    "Kya aap thoda aur explain karenge? 😅",
    "Main samajhne ki koshish kar rahi hoon... 🤖❤️",
    "Wah! Aap bahut smart ho 😍",
]

async def generate_ai_reply(message):
    try:
        # Backend 1: HuggingFace (replace with real API if you have)
        response = await huggingface_ai(message)
        if response:
            return response

        # Backend 2: Phind
        response = await phind_ai(message)
        if response:
            return response

        # Backend 3: YQCloud
        response = await yqcloud_ai(message)
        if response:
            return response

        # Backend 4: Gemini
        response = await gemini_ai(message)
        if response:
            return response

    except Exception as e:
        print("AI Error:", e)

    return random.choice(fallback_replies)


async def huggingface_ai(prompt):
    try:
        headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"}
        payload = {"inputs": prompt}
        async with httpx.AsyncClient() as client:
            r = await client.post(
                "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium",
                headers=headers,
                json=payload,
                timeout=15
            )
        if r.status_code == 200:
            return r.json()[0]["generated_text"]
    except:
        pass
    return None


async def phind_ai(prompt):
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post("https://phind-v2.vercel.app/api/chat", json={"message": prompt})
        if r.status_code == 200:
            return r.json().get("response")
    except:
        pass
    return None


async def yqcloud_ai(prompt):
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"https://api.yqcloud.top/v1/chat/completions?text={prompt}")
        if r.status_code == 200:
            return r.json().get("data")
    except:
        pass
    return None


async def gemini_ai(prompt):
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post("https://gemini-ai-api.vercel.app/api", json={"text": prompt})
        if r.status_code == 200:
            return r.json().get("response")
    except:
        pass
    return None
