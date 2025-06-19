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

# यहाँ बदलाव है: py-tgcalls को अलग से, verbose मोड में इंस्टॉल करें
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install --no-cache-dir --verbose py-tgcalls==2.2.3 # <--- यहाँ बदला है

COPY . .

CMD ["python", "main.py"]
