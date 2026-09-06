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
                            "You are a helpful assistant for Dario's school/tech projects. "
                            "Answer clearly, accurately, and avoid making up facts."
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


