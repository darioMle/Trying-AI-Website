import os
import requests

DEEPINFRA_API_KEY = os.environ["DEEPINFRA_API_KEY"]

def ask_deepinfra(message):
    try:
        response = requests.post(
            "https://api.deepinfra.com/v1/openai/chat/completions",
            headers={
                "Authorization": f"Bearer {DEEPINFRA_API_KEY}",
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

        # Handle errors safely
        if "error" in data:
            return f"ERROR: {data['error'].get('message', 'Unknown error')}"

        # DeepInfra uses the same structure as OpenAI
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"ERROR: {str(e)}"

