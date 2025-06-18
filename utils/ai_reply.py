import random
import httpx

async def get_ai_reply(message: str) -> str:
    try:
        async with httpx.AsyncClient(timeout=20) as client:
            response = await client.post(
                "https://yqcloud.ziyexin.xyz/api/gpt",
                json={"messages": [{"role": "user", "content": message}]}
            )
            data = response.json()
            return data.get("result", "Hmm... kuch samajh nahi aaya 😅")
    except Exception as e:
        fallback = [
            "Kya baat karni hai jaan? 💬",
            "Main hoon na, bolo ❤️",
            "Kuch interesting batao na 😍",
        ]
        return random.choice(fallback)
