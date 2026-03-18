from supabase import create_client, Client
from app.config import SUPABASE_URL, SUPABASE_KEY

# Initialize client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# 🔹 USER FUNCTIONS

def get_user(user_id: str):
    res = supabase.table("users").select("*").eq("id", user_id).execute()
    return res.data[0] if res.data else None


def create_user(user_id: str, email: str = "", plan: str = "free"):
    return supabase.table("users").insert({
        "id": user_id,
        "email": email,
        "plan": plan
    }).execute()


# 🔹 USAGE FUNCTIONS

def get_usage(user_id: str, date: str):
    res = supabase.table("usage") \
        .select("*") \
        .eq("user_id", user_id) \
        .eq("date", date) \
        .execute()

    return res.data[0] if res.data else None


def update_usage(user_id: str, date: str, count: int):
    return supabase.table("usage").update({
        "count": count
    }).eq("user_id", user_id).eq("date", date).execute()


def insert_usage(user_id: str, date: str):
    return supabase.table("usage").insert({
        "user_id": user_id,
        "date": date,
        "count": 1
    }).execute()


# 🔹 PAYMENT (FUTURE)

def update_user_plan(user_id: str, plan: str):
    return supabase.table("users").update({
        "plan": plan
    }).eq("id", user_id).execute()