import os
import requests

TOGETHER_API_KEY = os.environ["TOGETHER_API_KEY"]

def ask_together(message):
    try:
        response = requests.post(
            "https://api.together.ai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {TOGETHER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/Meta-Llama-3-8B-Instruct",
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

        if "error" in data:
            return f"ERROR: {data['error'].get('message', 'Unknown error')}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"ERROR: {str(e)}"


