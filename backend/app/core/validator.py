def validate_input(topic: str):
    if not topic:
        return False

    topic = topic.strip()

    if len(topic) < 3:
        return False

    if len(topic) > 200:
        return False

    return True