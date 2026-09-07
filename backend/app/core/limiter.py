from datetime import datetime
from collections import OrderedDict

from app.config import FREE_LIMIT

MAX_ENTRIES = 2000
DEFAULT_LIMIT = FREE_LIMIT

_usage: OrderedDict[str, dict[str, int]] = OrderedDict()


def _evict_if_needed():
    while len(_usage) > MAX_ENTRIES:
        _usage.popitem(last=False)


def check_limit(key: str, limit: int = DEFAULT_LIMIT) -> bool:
    """Check and increment daily usage for the given key (token or IP).

    Returns True if the request is allowed, False if the daily limit is reached.
    """
    today = str(datetime.now().date())

    if key not in _usage:
        _evict_if_needed()
        _usage[key] = {}
        _usage.move_to_end(key)

    bucket = _usage[key]

    if today not in bucket:
        bucket[today] = 0

    if bucket[today] >= limit:
        return False

    bucket[today] += 1
    _usage.move_to_end(key)
    return True
