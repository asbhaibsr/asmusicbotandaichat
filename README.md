# 🎧 AsMusicBot & AI Chat Assistant 🎶🤖

Welcome to **AsMusicBot & AI Chat Assistant** – a fully functional **Telegram Music Bot** with smart **AI Chat features** built in! This bot can **play music in group voice chats**, as well as **respond to users with intelligent AI replies** in a romantic, desi, or funny Hindi style!

---

## 🧠 Features

- 🎵 High-quality music streaming in group voice chats
- 🤖 Human-like female AI replies (romantic + smart chat)
- 🧠 AI memory with MongoDB (for unique replies)
- 🔁 Free AI backends like g4f, gemini, yqcloud
- 📥 Download YouTube audio (auto-convert to mp3)
- 🔧 Admin/Owner commands:
  - `/ai on` / `/ai off` to toggle AI chat
  - `/stats` for usage info
  - `/broadcast` to send messages to all groups
  - `/help`, `/settings` for control
- 🔒 Anti-spam group tools (like Rose bot)
- 📤 Forward private chats to owner with easy reply
- 📂 Docker ready for easy Koyeb deployment

---

## 🔗 Telegram Links

- 📽️ **Movie Search Group:** [@iStreamX](https://t.me/iStreamX)
- 📢 **Update Channel:** [@asbhai_bsr](https://t.me/asbhai_bsr)
- 👑 **Bot Owner:** [@asbhaibsr](https://t.me/asbhaibsr)

---

## 🚀 Deployment

This bot is ready for **Koyeb deployment** using **Dockerfile**.

### 📦 Deploy on Koyeb (Docker)
```bash
# Clone the repository
git clone https://github.com/yourusername/asmusicbotandaichat.git
cd asmusicbotandaichat

# Add your secrets to the environment:
#  - API_ID, API_HASH (from my.telegram.org)
#  - BOT_TOKEN (from BotFather)
#  - MONGO_URI (MongoDB URI)
#  - OWNER_ID (numeric)

# Build Docker and deploy on Koyeb
