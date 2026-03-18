cache_store = {}

def get_cache(prompt: str):
    return cache_store.get(prompt)


def set_cache(prompt: str, result: str):
    cache_store[prompt] = result