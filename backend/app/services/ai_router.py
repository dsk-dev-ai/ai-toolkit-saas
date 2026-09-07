import logging

from app.config import GEMINI_API_KEY

logger = logging.getLogger(__name__)

_client = None


def _get_client():
    global _client
    if _client is not None:
        return _client
    if not GEMINI_API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY environment variable is not set. "
            "Add it to your .env file or export it in your shell."
        )
    from google import genai
    _client = genai.Client(api_key=GEMINI_API_KEY)
    return _client


def generate_ai(prompt: str) -> str:
    try:
        client = _get_client()
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text if response.text else "No response"

    except RuntimeError:
        raise
    except Exception as e:
        logger.exception("AI generation failed")
        return "An error occurred while generating content. Please try again later."
