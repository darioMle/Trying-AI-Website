import os
import requests

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

def ask_openrouter(message):
    if not OPENROUTER_API_KEY:
        return "ERROR: OPENROUTER_API_KEY not set."

    try:
        resp = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3b-instruct",
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful assistant for Dario's Tech Repair. "
                            "Answer clearly and avoid making up facts."
                        )
                    },
                    {"role": "user", "content": message}
                ],
                "max_tokens": 512,
                "temperature": 0.2
            },
            timeout=30
        )

        data = resp.json()

        if resp.status_code != 200:
            # Try to return a readable error message from the API
            err = data.get("error") or data.get("message") or resp.text
            return f"ERROR: {err}"

        # Normal OpenAI-style response structure
        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]

        return "ERROR: No choices returned by OpenRouter."

    except requests.exceptions.RequestException as e:
        return f"ERROR: Network or timeout error: {str(e)}"
    except Exception as e:
        return f"ERROR: {str(e)}"

