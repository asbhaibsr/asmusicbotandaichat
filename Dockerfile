# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg git gcc libffi-dev libssl-dev python3-dev build-essential && \
    apt-get clean

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port for Koyeb health check
EXPOSE 8080

# Run the bot
CMD ["python3", "main.py"]
