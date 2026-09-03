import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Create OpenAI client using your Render environment variable
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def ask_openai(message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a friendly tech repair assistant for Dario's Tech Repair. "
                        "Answer questions using the shop's information, repair services, prices, "
                        "and policies. Keep answers short, helpful, and clear."
                    )
                },
                {"role": "user", "content": message}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"ERROR: {str(e)}"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_reply = ask_openai(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run()


