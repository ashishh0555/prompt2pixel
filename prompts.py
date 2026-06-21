import random

STYLE_MODIFIERS = {
    "Realistic": "photorealistic, highly detailed, natural lighting, 8k",
    "Anime": "anime style, detailed, vibrant colors",
    "Cyberpunk": "cyberpunk aesthetic, neon lights, futuristic, high contrast, cinematic",
    "Watercolor": "watercolor painting, soft brush strokes, pastel tones, artistic",
    "Fantasy Art": "fantasy art, epic, dramatic lighting, intricate detail, concept art",
    "3D Render": "3D render, studio lighting, octane render, highly detailed",
    "Sketch": "pencil sketch, hand-drawn, black and white, fine line art",
    "Minimalist": "minimalist, clean lines, simple shapes, flat colors",
}

STYLE_OPTIONS = list(STYLE_MODIFIERS.keys())


def build_prompt(user_prompt: str, style: str) -> str:
    """
    Combine the user's raw prompt with the chosen style's modifier.

    Example:
        build_prompt("A cat wearing sunglasses", "Anime")
        -> "A cat wearing sunglasses, anime style, detailed, vibrant colors."
    """
    cleaned = user_prompt.strip().rstrip(".")
    modifier = STYLE_MODIFIERS.get(style, "")

    if not cleaned:
        return ""
    if not modifier:
        return f"{cleaned}."
    return f"{cleaned}, {modifier}."

RANDOM_PROMPTS = [
    "A futuristic Indian city at night",
    "A dragon perched on a Himalayan peak at sunrise",
    "An astronaut having chai at a Mumbai street stall",
    "A treehouse village in a glowing forest",
    "A vintage steam train crossing a desert canyon",
    "A robot tending a rooftop garden in Tokyo",
    "An underwater library lit by bioluminescent fish",
    "A floating market above the clouds",
    "A lighthouse on a cliff during a meteor shower",
    "A samurai cat guarding a bamboo gate",
    "A monsoon evening on a Kerala backwater",
    "A clockwork owl perched in an old library",
]


def random_prompt() -> str:
    """Return a random example prompt to seed the text input with."""
    return random.choice(RANDOM_PROMPTS)
