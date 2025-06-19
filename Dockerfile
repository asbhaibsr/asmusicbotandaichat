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

# इस लाइन को मानक pip install पर वापस करें
RUN pip install --upgrade pip && pip install -r requirements.txt 

COPY . .

CMD ["python", "main.py"]
