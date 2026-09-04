import os
import requests

GROQ_API_KEY = os.environ["GROQ_API_KEY"]

def ask_groq(message):
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mixtral-8x7b-32768",
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are the official support assistant for Dario's Tech Repair. "
                            "Use ONLY the real business info: "
                            "Phone repairs, laptop repairs, data recovery, home tech support. "
                            "Locations: Edinburgh, Glasgow, Aberdeen. "
                            "Contact: support@dariotechrepair.com / 0131 555 1234. "
                            "Friendly Scottish tone. No made‑up prices."
                        )
                    },
                    {"role": "user", "content": message}
                ]
            }
        )

        data = response.json()

        # If Groq returned an error, show it safely
        if "error" in data:
            return f"ERROR: {data['error'].get('message', 'Unknown error')}"

        # If choices is missing, return a readable message
        if "choices" not in data:
            return "ERROR: Groq returned no choices."

        # Normal successful response
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"ERROR: {str(e)}"
