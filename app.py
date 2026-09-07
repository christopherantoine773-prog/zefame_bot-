import os
import time
from flask import Flask
import requests

app = Flask(__name__)

TIKTOK_LINK = "https://vt.tiktok.com/ZSqMtNsYH/"
VIEWS_URL = "https://zefame.com/en/free-tiktok-views"
LIKES_URL = "https://zefame.com/en/free-tiktok-likes"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://zefame.com/",
    "Origin": "https://zefame.com",
}

@app.route("/")
def home():
    return "Le bot Zefame (Vues & Likes) est en ligne !"

@app.route("/run-views")
def trigger_views():
    try:
        # Pause de 60 secondes pour simuler le temps d'attente du site
        time.sleep(60)
        response = requests.post(VIEWS_URL, headers=HEADERS, data={"url": TIKTOK_LINK}, timeout=45)
        if response.status_code == 200:
            return f"Vues - Succès ! Code : {response.status_code}", 200
        else:
            return f"Vues - Erreur site : {response.status_code}", 400
    except Exception as e:
        return f"Erreur technique (Vues) : {str(e)}", 500

@app.route("/run-likes")
def trigger_likes():
    try:
        # Pause de 60 secondes avant l'envoi des likes
        time.sleep(60)
        response = requests.post(LIKES_URL, headers=HEADERS, data={"url": TIKTOK_LINK}, timeout=45)
        if response.status_code == 200:
            return f"Likes - Succès ! Code : {response.status_code}", 200
        else:
            return f"Likes - Erreur site : {response.status_code}", 400
    except Exception as e:
        return f"Erreur technique (Likes) : {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
