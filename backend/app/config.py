import os
from dotenv import load_dotenv

load_dotenv()

# AI Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Supabase (future use)
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Razorpay (future use)
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_SECRET = os.getenv("RAZORPAY_SECRET")

# Limits
FREE_LIMIT = 5
PRO_LIMIT = 50
GLOBAL_LIMIT = 18