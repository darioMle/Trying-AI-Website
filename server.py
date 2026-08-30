from flask import Flask, request, jsonify
from chatbot import ask_huggingface

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_reply = ask_huggingface(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
