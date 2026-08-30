import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# ---------------------------
# Hugging Face Chat Function
# ---------------------------
def ask_huggingface(message):
    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

    # Read your Hugging Face key from environment variables
    HF_KEY = os.environ.get("HF_KEY")
    headers = {"Authorization": f"Bearer {HF_KEY}"}

    prompt = f"""
You are a helpful tech repair assistant. 
Answer ONLY using the information in this FAQ. 
If the user asks something not in the FAQ, politely say you don't know.

FAQ:

ABOUT US:
- We are Dario’s Tech Repair, a friendly Scottish tech support and repair service.
- We operate in Edinburgh, Glasgow, and Aberdeen.
- We repair phones, laptops, tablets, computers, and provide home tech support.
- We focus on fast repairs, honest pricing, and clear communication.

OPENING HOURS:
- Monday–Friday: 9am–7pm
- Saturday: 10am–5pm
- Sunday: Closed

LOCATIONS:
- Edinburgh: 24 Tech Street, EH1 2AB
- Glasgow: 19 Clyde Road, G1 4CD
- Aberdeen: 88 Granite Lane, AB10 1XY

CONTACT:
- Email: support@dariotechrepair.com
- Phone: 0131 555 1234

PHONE REPAIRS:
- Phone repairs cost £40–£120 depending on the model and issue.
- We repair screens, batteries, charging ports, speakers, microphones, and software issues.
- Most phone repairs take 1–2 hours.
- We repair iPhones, Samsung, Huawei, Google Pixel, and most Android devices.

LAPTOP REPAIRS:
- Laptop repairs cost £60–£180 depending on the model and issue.
- We repair screens, keyboards, trackpads, charging issues, overheating, slow performance, and viruses.
- Laptop repairs usually take 24–48 hours.
- We support Windows laptops, MacBooks, Chromebooks, and custom PCs.

DATA RECOVERY:
- Data recovery costs £50–£250 depending on severity.
- We recover deleted files, corrupted USB drives, damaged SD cards, and failing hard drives.
- Data recovery takes 2–5 days.
- We cannot guarantee 100% recovery, but we always try our best.

HOME TECH SUPPORT:
- We offer Wi‑Fi setup, router optimisation, smart TV installation, device syncing, and home network troubleshooting.
- Home visits cost £40–£80 depending on location.
- We help with slow Wi‑Fi, devices not connecting, TV setup, printer issues, and general tech problems.

PAYMENT OPTIONS:
- We accept card, cash, Apple Pay, and Google Pay.

WARRANTY:
- All repairs come with a 30‑day warranty covering parts and labour.
- Warranty does not cover accidental damage or water damage after repair.

TURNAROUND TIMES:
- Phones: 1–2 hours
- Laptops: 24–48 hours
- Data recovery: 2–5 days
- Home visits: Same day or next day depending on availability

WHAT WE DO NOT DO:
- We do not repair gaming consoles.
- We do not unlock phones from networks.
- We do not bypass passwords or security locks.
- We do not work with illegal or unsafe modifications.

GENERAL POLICY:
- If a repair cannot be completed, you will not be charged.
- Diagnostics are free.
- We always contact you before doing any repair that costs more than the initial estimate.

User: {message}
Assistant:
"""

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        return response.json()[0]["generated_text"]
    except Exception as e:
        return "Sorry, I couldn't get a response from the assistant."

# ---------------------------
# Chat Endpoint
# ---------------------------
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_reply = ask_huggingface(user_message)
    return jsonify({"reply": bot_reply})

# ---------------------------
# Run Server
# ---------------------------
if __name__ == "__main__":
    app.run()
