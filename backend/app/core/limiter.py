from datetime import datetime

LIMIT = 5
usage = {}

def check_limit(user_id: str):
    today = str(datetime.now().date())

    if user_id not in usage:
        usage[user_id] = {}

    if today not in usage[user_id]:
        usage[user_id][today] = 0

    if usage[user_id][today] >= LIMIT:
        return False

    usage[user_id][today] += 1
    return True