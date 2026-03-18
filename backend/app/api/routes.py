from fastapi import APIRouter
from app.models.schemas import GenerateRequest
from app.core.validator import validate_input
from app.core.limiter import check_limit
from app.core.cache import get_cache, set_cache
from app.core.security import verify_user
from app.services.prompts import build_prompt
from app.services.ai_router import generate_ai

router = APIRouter()

@router.post("/generate")
async def generate_content(data: GenerateRequest):
    topic = data.topic
    user_id = data.user_id

    # Security
    if not verify_user(user_id):
        return {"error": "Unauthorized"}

    # Validation
    if not validate_input(topic):
        return {"error": "Invalid input"}

    # Limit check
    if not check_limit(user_id):
        return {"error": "Daily limit reached"}

    # Prompt
    prompt = build_prompt(topic)

    # Cache
    cached = get_cache(prompt)
    if cached:
        return {"result": cached, "source": "cache"}

    # AI
    result = generate_ai(prompt)

    # Save cache
    set_cache(prompt, result)

    return {"result": result, "source": "ai"}