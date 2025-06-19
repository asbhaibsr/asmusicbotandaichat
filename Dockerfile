FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    ffmpeg \
    libsm6 \
    libxext6 \
    zlib1g-dev \
    libjpeg-dev \
    pkg-config \
    git \
    libsodium-dev \
    libopus-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

# pyrogram-voice-chat को सीधे GitHub से इंस्टॉल करें
RUN pip install git+https://github.com/pyrogram/pyrogram-voice-chat.git # <--- यहाँ नया बदलाव

COPY . .

CMD ["python", "main.py"]
