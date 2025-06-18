import random
import httpx

async def chat_with_ai(prompt: str, user_id: int = 0) -> str:
    try:
        # Gemini API (fast and stable - recommended)
        url = "https://chatgpt.ai4freeapi.repl.co/v1/gemini"
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json={"prompt": prompt})
            if response.status_code == 200:
                data = response.json()
                if "text" in data:
                    return data["text"].strip()

        # Fallback to yqcloud GPT-3.5 if Gemini fails
        url = "https://chatgpt.yqcloud.top/api/ai"
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json={"text": prompt})
            if response.status_code == 200:
                data = response.json()
                if "content" in data:
                    return data["content"].strip()

        # Last fallback to gptgo
        url = f"https://gptgo.ai/api/conversation"
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json={"message": prompt})
            if response.status_code == 200:
                data = response.json()
                if "response" in data:
                    return data["response"].strip()

        return (
            "🥺 Maaf karo dosto, abhi AI thoda busy hai.\n"
            "Tab tak movie chahiye? Join karo humara movie group 🎬\n👉 @iStreamX"
        )

    except Exception as e:
        return (
            "🥺 Kuch gadbad ho gayi... AI abhi reply nahi kar pa rahi.\n"
            "Tab tak bore ho to join karo humara movie group 👉 @iStreamX 🎥"
        )
