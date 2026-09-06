import os
import requests

OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]

def ask_openrouter(message):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/Meta-Llama-3-8B-Instruct",
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful assistant for Dario's school and tech projects. "
                            "Answer clearly and avoid making up facts."
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
