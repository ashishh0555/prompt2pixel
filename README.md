# 🎨 Prompt2Pixel — AI Image Generation Chatbot

A simple Streamlit web app that turns a text prompt + style choice into an
AI-generated image, using the Stability AI API (Stable Image Core).

## What it does

Type a description, pick an art style (Anime, Cyberpunk, Watercolor, etc.),
and hit **Generate**. The app rewrites your prompt to bake in the style
(e.g. `"A cat wearing sunglasses"` + *Anime* →
`"A cat wearing sunglasses, anime style, detailed, vibrant colors."`),
sends it to the image generation API, and displays the result.

**Core features**
- Title + description, text prompt input, style radio buttons, Generate
  button, image display, prompt history — per the assignment spec.
- Style-conditioned prompt building (`prompts.py`).
- No hardcoded keys — reads `STABILITY_API_KEY` from a `.env` file locally
  or from Streamlit Secrets when deployed.

**Bonus features included**
- 🖼️ Gallery view of every image generated this session
- ⬇️ Download button for each generated image
- 📐 Aspect ratio selector (Square / Portrait / Landscape / Widescreen / Tall)
- 🚫 Negative prompt input
- 🔢 Generate 1–4 images at once
- 🎲 Random prompt generator

> Light/dark mode isn't reimplemented here — Streamlit already ships a
> native theme switcher (the **⋮** menu in the top-right corner →
> **Settings** → Theme), so a custom toggle would just duplicate it.

## File structure

```
Prompt2Pixel/
├── app.py                      # Streamlit UI — layout & user interaction only
├── api_client.py                # All Stability AI API calls
├── prompts.py                   # Style modifiers + prompt building + random prompts
├── utils.py                     # Session state, image<->bytes, theme CSS, aspect ratios
├── requirements.txt
├── .env.example                 # Template for your local .env
├── .streamlit/
│   └── secrets.toml.example     # Template for Streamlit Cloud secrets
└── .gitignore
```

## Run it locally

```bash
# 1. Clone and enter the repo
git clone <your-repo-url>
cd Prompt2Pixel

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API key (see below), then run
streamlit run app.py
```

The app opens at `http://localhost:8501`.

## Adding your API key

1. Create a free account at [platform.stability.ai](https://platform.stability.ai).
2. Go to **Account → API Keys** (`platform.stability.ai/account/keys`) and
   create a new key. New accounts get a one-time batch of free trial
   credits to test with.
3. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
4. Open `.env` and paste your key:
   ```
   STABILITY_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
   ```

`.env` is git-ignored, so your key never gets committed. Locally, `app.py`
loads it via `python-dotenv`; `api_client.py` reads it from
`os.environ["STABILITY_API_KEY"]`.

## Deploying

### Streamlit Community Cloud (recommended, free)

1. Push this project to a public (or private) GitHub repo — **make sure
   `.env` is NOT committed** (it's already in `.gitignore`).
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**.
3. Pick your repo, branch, and set the main file path to `app.py`.
4. Before deploying, open **Advanced settings → Secrets** and paste:
   ```toml
   STABILITY_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"
   ```
5. Click **Deploy**. `api_client.py` automatically falls back to
   `st.secrets["STABILITY_API_KEY"]` when no environment variable is set,
   so no code changes are needed between local and deployed environments.

### Render / Railway

Both work too — set `STABILITY_API_KEY` as an environment variable in the
platform's dashboard (not in a committed file), and use
`streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
as the start command.

## Known limitations

- **Credit-based billing, not an unlimited free tier.** Stability AI gives
  new accounts a one-time batch of free trial credits; after that, each
  generation consumes paid credits from your account. Check your balance
  at `platform.stability.ai/account/credits` if generation suddenly stops
  working.
- **Aspect ratio, not exact pixel dimensions.** Stable Image Core controls
  output shape via an `aspect_ratio` parameter (it always renders at
  roughly 1 megapixel), rather than letting you request an exact width
  and height — that's why the size picker in this app is framed as
  "aspect ratio" rather than a literal pixel size.

## Tech stack

Python · Streamlit · Stability AI (Stable Image Core API) · Pillow ·
python-dotenv · requests

