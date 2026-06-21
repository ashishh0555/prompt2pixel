from io import BytesIO

import streamlit as st

ASPECT_RATIOS = {
    "Square (1:1)": "1:1",
    "Portrait (2:3)": "2:3",
    "Landscape (3:2)": "3:2",
    "Widescreen (16:9)": "16:9",
    "Tall (9:16)": "9:16",
}


def init_session_state():
    """Create the session-state keys this app relies on, once per session."""
    if "history" not in st.session_state:
        st.session_state.history = []  # list of past generations
    if "prompt_input" not in st.session_state:
        st.session_state.prompt_input = ""


def image_to_bytes(image) -> bytes:
    """Convert a PIL.Image to PNG bytes, for use with st.download_button."""
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()
