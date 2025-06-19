from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Alive!", 200

def run():
    # Flask dev server, Koyeb health check के लिए पर्याप्त है
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    # थ्रेड में Flask सर्वर स्टार्ट करें
    threading.Thread(target=run, daemon=True).start()
