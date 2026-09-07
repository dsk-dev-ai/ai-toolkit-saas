from fastapi import APIRouter, Depends, HTTPException, Request

from app.models.schemas import GenerateRequest
from app.core.validator import validate_input
from app.core.limiter import check_limit
from app.core.cache import get_cache, set_cache
from app.core.security import get_api_identity
from app.config import FREE_LIMIT
from app.services.prompts import build_prompt
from app.services.ai_router import generate_ai

router = APIRouter()


@router.post("/generate")
async def generate_content(data: GenerateRequest, request: Request, token: str = Depends(get_api_identity)):
    topic = data.topic

    if not validate_input(topic):
        raise HTTPException(status_code=400, detail="Invalid input")

    rate_key = token
    client_ip = request.client.host if request.client else "unknown"
    if not check_limit(rate_key):
        raise HTTPException(status_code=429, detail="Daily limit reached")

    prompt = build_prompt(topic)

    cached = get_cache(prompt)
    if cached:
        return {"result": cached, "source": "cache"}

    result = generate_ai(prompt)

    set_cache(prompt, result)

    return {"result": result, "source": "ai"}
