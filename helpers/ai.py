import random

async def get_ai_reply(messages):
    # Random AI-style girl replies
    responses = [
        "Awww 😳 sachii?",
        "Haww! 😅 tum toh naughty nikle 😜",
        "Mujhe laga tum kuch kehna chahte ho 💕",
        "Kya yeh sach hai ya sapna? 😌",
        "Tumhare bina bot adhura hai 😘",
        "Pehle aisa koi nahi mila mujhe 🥺",
        "Tum baatein achhi karte ho 💫",
        "Acha laga sunke 💖",
        "Baaton mein dum hai tumhari 😉",
        "Hmm... interesting 🤔"
    ]
    return random.choice(responses)
