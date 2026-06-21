import os
from io import BytesIO

import requests
import streamlit as st
from PIL import Image

API_HOST = "https://api.stability.ai"

ENDPOINT = f"{API_HOST}/v2beta/stable-image/generate/core"


def _get_api_key() -> str:
    """Resolve the Stability AI key from env vars or Streamlit secrets."""
    key = os.getenv("STABILITY_API_KEY")

    if not key:
        try:
            key = st.secrets["STABILITY_API_KEY"]
        except Exception:
            key = None

    if not key:
        raise RuntimeError(
            "STABILITY_API_KEY not found. Add it to a local .env file, or to "
            "your Streamlit Cloud app's Secrets (see README.md) before generating images."
        )
    return key


def generate_image(prompt: str, negative_prompt: str = "", aspect_ratio: str = "1:1"):
    """
    Generate a single image from a prompt via Stable Image Core.

    Returns a PIL.Image.Image object.
    """
    form_data = {
        "prompt": prompt,
        "output_format": "png",
        "aspect_ratio": aspect_ratio,
    }
    if negative_prompt.strip():
        form_data["negative_prompt"] = negative_prompt.strip()

    response = requests.post(
        ENDPOINT,
        headers={
            "authorization": f"Bearer {_get_api_key()}",
            "accept": "image/*",
        },
        
        files={"none": ""},
        data=form_data,
        timeout=60,
    )

    if response.status_code != 200:
        
        try:
            detail = response.json()
        except ValueError:
            detail = response.text
        raise RuntimeError(f"Stability AI error {response.status_code}: {detail}")

    return Image.open(BytesIO(response.content))


def generate_images(prompt: str, negative_prompt: str = "", num_images: int = 1,
                     aspect_ratio: str = "1:1"):
    """
    Generate one or more images from the same prompt.

    Returns a list of PIL.Image.Image objects. Each call is a separate
    request -- Stable Image Core has no native "batch" parameter.
    """
    return [
        generate_image(prompt, negative_prompt=negative_prompt, aspect_ratio=aspect_ratio)
        for _ in range(num_images)
    ]
