def ask_huggingface(message):
    API_URL = "https://api-inference.huggingface.co/models/google/gemma-2b-it"
    HF_KEY = os.environ.get("HF_KEY")

    headers = {"Authorization": f"Bearer {HF_KEY}"}

    payload = {
        "inputs": f"User: {message}\nAssistant:",
        "parameters": {"max_new_tokens": 200}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()

        # Debug print
        print("HF RESPONSE:", data)

        # Case 1: dict with generated_text
        if isinstance(data, dict) and "generated_text" in data:
            return data["generated_text"]

        # Case 2: list with generated_text
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]

        # Case 3: error from HF
        if "error" in data:
            return f"HF ERROR: {data['error']}"

        return "Sorry, I couldn't get a response from the assistant."

    except Exception as e:
        return f"HF ERROR: {str(e)}"

