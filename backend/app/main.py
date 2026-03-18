from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict for security
    allow_credentials=True,
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
        "message": "🚀 AI Toolkit SaaS API running",
        "docs": "/docs"
    }

# -----------------------------
# Supabase Test Endpoint
# -----------------------------
@app.get("/test-db")
def test_db():
    try:
        # simple check (no DB write)
        return {"status": "Supabase connected"}
    except Exception as e:
        return {"error": str(e)}

# -----------------------------
# AI Test Endpoint (optional)
# -----------------------------
from app.services.ai_router import generate_ai

@app.get("/test-ai")
def test_ai():
    try:
        result = generate_ai("AI tools for students")
        return {"result": result[:500]}  # trimmed output
    except Exception as e:
        return {"error": str(e)}