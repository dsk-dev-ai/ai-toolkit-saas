def build_prompt(topic: str):
    return f"""
Generate the following content on topic: {topic}

1. Blog (300 words, SEO optimized with headings)
2. 3 Tweets (short and engaging)
3. YouTube Script (1 minute, hook + value + CTA)

Keep response clear and structured.
"""