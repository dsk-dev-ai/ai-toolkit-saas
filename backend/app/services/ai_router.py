from google import genai
from app.config import GEMINI_API_KEY

# Create client
client = genai.Client(api_key=GEMINI_API_KEY)


def generate_ai(prompt: str):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text if response.text else "No response"

    except Exception as e:
        return f"AI Error: {str(e)}"