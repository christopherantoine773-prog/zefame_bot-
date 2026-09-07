import os
from flask import Flask
import requests

app = Flask(__name__)

TIKTOK_LINK = "https://vt.tiktok.com/ZSqMtNsYH/"
TARGET_URL = "https://zefame.com/en/free-tiktok-views"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://zefame.com/en/free-tiktok-views",
    "Origin": "https://zefame.com",
}

@app.route("/")
def home():
    return "Le bot Zefame est en ligne !"

@app.route("/run")
def trigger_bot():
    try:
        response = requests.post(TARGET_URL, headers=HEADERS, data={"url": TIKTOK_LINK}, timeout=30)
        if response.status_code == 200:
            return f"Succès ! Code réponse : {response.status_code}", 200
        else:
            return f"Le site a répondu avec le code : {response.status_code}", 400
    except Exception as e:
        return f"Erreur technique : {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
