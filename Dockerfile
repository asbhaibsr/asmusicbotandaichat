FROM python:3.10

# Install git, ffmpeg, gcc for audio & dependency builds
RUN apt update && apt install -y git ffmpeg gcc

# Set working directory inside container
WORKDIR /app

# Copy all project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Start your bot
CMD ["python3", "main.py"]
