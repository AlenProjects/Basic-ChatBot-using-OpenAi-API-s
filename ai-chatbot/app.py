# app.py
from flask import Flask, render_template, request, jsonify, send_file
import uuid
import json
import os
from datetime import datetime

app = Flask(__name__)

CHAT_FILE = "chat_data.json"

# Ensure chat data file exists
if not os.path.exists(CHAT_FILE):
    with open(CHAT_FILE, "w") as f:
        json.dump({}, f)


def load_chats():
    with open(CHAT_FILE, "r") as f:
        return json.load(f)


def save_chats(chats):
    with open(CHAT_FILE, "w") as f:
        json.dump(chats, f, indent=2)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chats", methods=["GET"])
def get_chats():
    chats = load_chats()
    return jsonify([
        {"id": cid, "title": chat["title"]} for cid, chat in chats.items()
    ])


@app.route("/chat", methods=["POST"])
def create_chat():
    chats = load_chats()
    chat_id = str(uuid.uuid4())
    chats[chat_id] = {
        "title": f"Chat {len(chats) + 1}",
        "history": []
    }
    save_chats(chats)
    return jsonify({"chat_id": chat_id})


@app.route("/chat/<chat_id>", methods=["GET"])
def get_chat(chat_id):
    chats = load_chats()
    chat = chats.get(chat_id)
    if not chat:
        return jsonify({"error": "Chat not found"}), 404
    return jsonify(chat)


@app.route("/chat/<chat_id>", methods=["POST"])
def send_message(chat_id):
    data = request.get_json()
    user_input = data.get("user_input", "")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    chats = load_chats()
    if chat_id not in chats:
        return jsonify({"error": "Chat not found"}), 404

    # Dummy GPT response (replace with actual call)
    bot_response = f"Echo: {user_input}"

    chats[chat_id]["history"].append({"role": "user", "content": user_input})
    chats[chat_id]["history"].append({"role": "assistant", "content": bot_response})
    save_chats(chats)

    return jsonify({"response": bot_response})


@app.route("/chat/<chat_id>", methods=["DELETE"])
def delete_chat(chat_id):
    chats = load_chats()
    if chat_id in chats:
        del chats[chat_id]
        save_chats(chats)
        return jsonify({"message": "Chat deleted"})
    return jsonify({"error": "Chat not found"}), 404


@app.route("/chat/<chat_id>/export", methods=["GET"])
def export_chat(chat_id):
    chats = load_chats()
    if chat_id not in chats:
        return jsonify({"error": "Chat not found"}), 404

    filename = f"chat_{chat_id}.json"
    filepath = os.path.join("exports", filename)
    os.makedirs("exports", exist_ok=True)

    with open(filepath, "w") as f:
        json.dump(chats[chat_id], f, indent=2)

    return send_file(filepath, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)