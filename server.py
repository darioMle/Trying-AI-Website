from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import ask_openai

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_reply = ask_openai(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run()
