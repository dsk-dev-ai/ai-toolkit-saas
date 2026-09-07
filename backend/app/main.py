from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import CORS_ORIGINS

# Routers
from app.api.routes import router as api_router
from app.api.health import health_router


# App instance
app = FastAPI(
    title="AI Toolkit SaaS",
    version="1.0.0",
    description="AI SaaS using Gemini + FastAPI"
)

# -----------------------------
# CORS (for frontend connection)
# -----------------------------
credentials_allowed = CORS_ORIGINS != ["*"] and len(CORS_ORIGINS) > 0

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=credentials_allowed,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Routes
# -----------------------------
app.include_router(api_router)
app.include_router(health_router)

# -----------------------------
# Root endpoint
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "AI Toolkit SaaS API running",
        "docs": "/docs"
    }
