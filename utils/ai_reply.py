import random
import httpx

async def get_ai_reply(message: str) -> str:
    try:
        async with httpx.AsyncClient(timeout=20) as client:
            url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
            headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"}
            payload = {"inputs": message}
            response = await client.post(url, json=payload, headers=headers)
            result = response.json()
            return result.get("generated_text", "Kya kehna chahti ho tum? 😅")
    except Exception as e:
        fallback = [
            "Hmm... interesting! 😊",
            "Zyada socho mat, bas enjoy karo. 😄",
            "Main hoon na! 💕",
        ]
        return random.choice(fallback)
