# Ek acchi base image use karein (Python version ke hisaab se)
FROM python:3.9-slim-buster

# Working directory set karein
WORKDIR /app

# Ab yeh naya step hai: System dependencies install karna
# Yeh woh tools aur libraries hain jo aapke Python packages ko install hone ke liye chahiye
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

# Ab aapki requirements.txt file copy karein
COPY requirements.txt .

# Ab Python dependencies install karein
RUN pip install --upgrade pip && pip install -r requirements.txt

# Ab baki ka application code copy karein
COPY . .

# Agar aapka app kisi port par run hota hai, toh usko expose karein (Koyeb ke liye)
# EXPOSE 8000 # Example port, aapke app ke hisaab se hoga

# Aapka app chalane ka command
# CMD ["python", "main.py"] # Isko apne main application file ke hisaab se badal lein
