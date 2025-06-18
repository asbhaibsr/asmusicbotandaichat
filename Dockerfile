# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install required system packages
RUN apt-get update && \
    apt-get install -y ffmpeg gcc libffi-dev libssl-dev python3-dev build-essential && \
    apt-get clean

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Run the bot
CMD ["python3", "bot.py"]
