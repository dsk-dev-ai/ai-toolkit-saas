import secrets
import logging

from fastapi import Header, HTTPException, Request

from app.config import API_TOKEN

logger = logging.getLogger(__name__)


async def get_api_identity(request: Request, authorization: str | None = Header(None)) -> str:
    """Validate Bearer token from Authorization header.

    Returns a canonical identity string (the bearer token) for rate-limiting.
    Raises HTTP 401 if missing or invalid.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(status_code=401, detail="Invalid Authorization header format")

    token = parts[1]

    if not API_TOKEN:
        logger.error("API_TOKEN is not configured")
        raise HTTPException(status_code=401, detail="Server authentication not configured")

    if not secrets.compare_digest(token, API_TOKEN):
        logger.warning("Invalid token attempt from %s", request.client.host if request.client else "unknown")
        raise HTTPException(status_code=401, detail="Invalid token")

    return token
