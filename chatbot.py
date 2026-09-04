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
                "model": "llama3-8b-8192",
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
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"ERROR: {str(e)}"


    except Exception as e:
        return f"ERROR: {str(e)}"

