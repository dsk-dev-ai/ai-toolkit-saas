import os
from dotenv import load_dotenv

load_dotenv()

# AI Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Auth
API_TOKEN = os.getenv("API_TOKEN", "")

# CORS (comma-separated origins)
CORS_ORIGINS_RAW = os.getenv("CORS_ORIGINS", "http://localhost:3000")
CORS_ORIGINS: list[str] = [
    o.strip() for o in CORS_ORIGINS_RAW.split(",") if o.strip()
]

# Supabase (future use)
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

# Razorpay (future use)
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_SECRET = os.getenv("RAZORPAY_SECRET")

# Limits
FREE_LIMIT = int(os.getenv("FREE_LIMIT", "5"))
PRO_LIMIT = int(os.getenv("PRO_LIMIT", "50"))
