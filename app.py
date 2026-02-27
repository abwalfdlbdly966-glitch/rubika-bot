from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("HHFJE0LPCJRIUREIMFORYJJXJLOVVMJATQYMYKFVTENKXQGMQZNYIHJKUSYQQCMK")
API_URL = f"https://botapi.rubika.ir/v3/{TOKEN}/"

def send_message(chat_id, text, buttons=None):
    data = {
        "chat_id": chat_id,
        "text": text
    }

    if buttons:
        data["inline_keyboard"] = buttons

    requests.post(API_URL + "sendMessage", json=data)

@app.route('/', methods=['POST'])
def webhook():
    update = request.json

    if "message" in update:
        chat_id = update["message"]["chat_id"]
        text = update["message"].get("text", "")

        if text == "/start":
            buttons = [
                [
                    {"text": "رول پلی", "callback_data": "roleplay"},
                    {"text": "اسکای بلاک", "callback_data": "skyblock"}
                ]
            ]

            send_message(chat_id, "یکی رو انتخاب کن 🎮", buttons)

    if "callback_query" in update:
        chat_id = update["callback_query"]["message"]["chat_id"]
        data = update["callback_query"]["data"]

        if data == "roleplay":
            send_message(chat_id, "وارد بخش رول پلی شدی 🎭")

        elif data == "skyblock":
            send_message(chat_id, "وارد بخش اسکای بلاک شدی 🏝")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
