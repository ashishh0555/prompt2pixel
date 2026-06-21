from datetime import datetime

from dotenv import load_dotenv
import streamlit as st

load_dotenv()

from prompts import STYLE_OPTIONS, build_prompt, random_prompt
from api_client import generate_images
from utils import ASPECT_RATIOS, image_to_bytes, init_session_state

st.set_page_config(page_title="Prompt2Pixel", page_icon="🎨", layout="wide")
init_session_state()

st.title("🎨 Prompt2Pixel")
st.write(
    "Describe what you want to see, pick an art style, and Prompt2Pixel "
    "turns it into an AI-generated image right in your browser."
)

def _randomize_prompt():
    st.session_state.prompt_input = random_prompt()


def _reuse_prompt(text: str):
    st.session_state.prompt_input = text


# sidebar

with st.sidebar:
    st.header("⚙️ Settings")

    aspect_label = st.selectbox("Aspect ratio", list(ASPECT_RATIOS.keys()), index=0)
    num_images = st.slider("Number of images", min_value=1, max_value=4, value=1)
    negative_prompt = st.text_input(
        "Negative prompt (optional)",
        placeholder="e.g. blurry, watermark, extra limbs",
        help="Describe what you do NOT want to see in the image.",
    )

    st.divider()
    st.subheader("🕘 Recent prompts")
    if st.session_state.history:
        for i, entry in enumerate(reversed(st.session_state.history[-8:])):
            label = f"{entry['style']} · {entry['prompt'][:28]}"
            st.button(
                label,
                key=f"hist_btn_{i}",
                on_click=_reuse_prompt,
                args=(entry["prompt"],),
                use_container_width=True,
            )
        if st.button("🗑️ Clear history", use_container_width=True):
            st.session_state.history = []
            st.rerun()
    else:
        st.caption("Nothing generated yet this session.")

input_col, random_col = st.columns([5, 1])
with input_col:
    user_prompt = st.text_input(
        "Describe the image you want",
        placeholder="A futuristic Indian city at night",
        key="prompt_input",
    )
with random_col:
    st.write("")
    st.write("")
    st.button("🎲 Random", on_click=_randomize_prompt, use_container_width=True)

style = st.radio("Style", STYLE_OPTIONS, horizontal=True)

if user_prompt.strip():
    st.caption(f"Final prompt sent to the API: _{build_prompt(user_prompt, style)}_")

generate_clicked = st.button("✨ Generate", type="primary")

if generate_clicked:
    if not user_prompt.strip():
        st.warning("Type a prompt first.")
    else:
        final_prompt = build_prompt(user_prompt, style)
        aspect_ratio = ASPECT_RATIOS[aspect_label]

        with st.spinner("Generating your image..."):
            images = None
            try:
                images = generate_images(
                    final_prompt,
                    negative_prompt=negative_prompt,
                    num_images=num_images,
                    aspect_ratio=aspect_ratio,
                )
            except Exception as exc:
                st.error(
                    f"Generation failed: {exc}\n\n"
                    "Double-check your STABILITY_API_KEY and that your "
                    "account still has credits — see README.md."
                )

        if images:
            st.session_state.history.append(
                {
                    "prompt": user_prompt,
                    "final_prompt": final_prompt,
                    "style": style,
                    "images": images,
                    "time": datetime.now().strftime("%H:%M:%S"),
                }
            )
            st.success(f"Done — generated {len(images)} image(s).")
            result_cols = st.columns(len(images))
            for idx, (col, img) in enumerate(zip(result_cols, images)):
                with col:
                    st.image(img, use_container_width=True)
                    st.download_button(
                        "⬇️ Download",
                        data=image_to_bytes(img),
                        file_name=f"promptcanvas_{idx + 1}.png",
                        mime="image/png",
                        key=f"dl_{idx}_{datetime.now().timestamp()}",
                    )

if st.session_state.history:
    st.divider()
    with st.expander(f"🖼️ Gallery ({len(st.session_state.history)} generations this session)"):
        for entry in reversed(st.session_state.history):
            st.markdown(f"**{entry['time']}** · _{entry['style']}_ · {entry['prompt']}")
            thumb_cols = st.columns(len(entry["images"]))
            for col, img in zip(thumb_cols, entry["images"]):
                with col:
                    st.image(img, use_container_width=True)
            st.markdown("---")
