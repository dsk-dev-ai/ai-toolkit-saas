import hashlib
from collections import OrderedDict

MAX_CACHE_ENTRIES = 500

_cache: OrderedDict[str, str] = OrderedDict()


def _evict_if_needed():
    while len(_cache) > MAX_CACHE_ENTRIES:
        _cache.popitem(last=False)


def _prompt_hash(prompt: str) -> str:
    return hashlib.sha256(prompt.encode()).hexdigest()


def get_cache(prompt: str) -> str | None:
    key = _prompt_hash(prompt)
    if key in _cache:
        _cache.move_to_end(key)
        return _cache[key]
    return None


def set_cache(prompt: str, result: str):
    key = _prompt_hash(prompt)
    _cache[key] = result
    _cache.move_to_end(key)
    _evict_if_needed()
