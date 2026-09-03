import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def ask_openai(message):
    try:
        response = client.responses.create(
            model="gpt-5.4-mini",
            input=[
                {
                    "role": "system",
                    "content": (
                        "You are a friendly tech repair assistant for Dario's Tech Repair. "
                        "Answer questions using the shop's information, repair services, prices, "
                        "and policies. Keep answers short, helpful, and clear."
                    )
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response.output_text

    except Exception as e:
        return f"ERROR: {str(e)}"
