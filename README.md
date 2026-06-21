# 🎨 Prompt2Pixel

Prompt2Pixel is an AI-powered image generation application built with Streamlit and Stability AI. Users can describe an image in natural language, select an artistic style, and generate high-quality AI images directly in the browser.

This project was developed as part of the Gen AI Bootcamp Week 3 assignment and demonstrates practical applications of prompt engineering in image generation.

---

## 🚀 Features

### 🎭 Style Conditioning

Enhances user prompts with style-specific modifiers before sending them to the image model.

Available styles:

* Realistic
* Anime
* Cyberpunk
* Watercolor
* Fantasy Art
* 3D Render
* Sketch
* Minimalist

---

### 🧠 Prompt Engineering Techniques

This project demonstrates:

* Style Conditioning
* Prompt Augmentation
* Negative Prompting
* Controlled Image Generation

---

### 🖼️ AI Image Generation

Generate one or multiple AI-generated images using Stability AI's Stable Image Core model.

---

### 🎲 Random Prompt Generator

Generate creative prompt ideas instantly using the built-in random prompt feature.

Examples:

* A futuristic Indian city at night
* An astronaut having chai at a Mumbai street stall
* A floating market above the clouds

---

### ❌ Negative Prompting

Specify unwanted elements such as:

* blurry
* watermark
* extra limbs
* low quality

to improve image quality and control output.

---

### 📐 Aspect Ratio Selection

Supported aspect ratios:

* Square (1:1)
* Portrait (2:3)
* Landscape (3:2)
* Widescreen (16:9)
* Tall (9:16)

---

### 📥 Download Generated Images

Download generated images directly as PNG files.

---

### 🕘 Prompt History & Gallery

* Stores generated prompts during the session
* Allows reuse of previous prompts
* Displays generated images in a gallery view

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Stability AI API
* Pillow (PIL)
* Requests
* Python Dotenv

---

## 📂 Project Structure

```text
prompt2pixel/
│
├── app.py
├── api_client.py
├── prompts.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── screenshots/
```

### File Responsibilities

#### app.py

Handles:

* User Interface
* User Interaction
* Gallery Display
* History Management

#### prompts.py

Handles:

* Style Conditioning
* Prompt Augmentation
* Random Prompt Generation

#### api_client.py

Handles:

* Stability AI API Integration
* Authentication
* Image Generation Requests
* Error Handling

#### utils.py

Handles:

* Session State Initialization
* Image Download Conversion
* Aspect Ratio Mapping

---


## 🌐 Live Demo

[Try the App Here](https://prompt2pixel-halnbvhlixbzuken4c883j.streamlit.app/)

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/ashishh0555/prompt2pixel.git
cd prompt2pixel
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Create Environment File

Create a `.env` file:

```env
STABILITY_API_KEY=YOUR_API_KEY
```

---

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 Learning Outcomes

Through this project I learned:

* Prompt Engineering for Image Generation
* Style Conditioning Techniques
* Negative Prompting
* API Integration
* Streamlit Application Development
* Session State Management
* Project Modularization
* AI-Powered Content Generation

---

## 🔮 Future Improvements

* Image Variation Generation
* Image Editing Support
* More Artistic Styles
* Image Upscaling
* User Authentication
* Image Sharing Features
* Advanced Prompt Templates

---

## 👨‍💻 Author

**Ashish Kumar**

B.Tech Electrical & Electronics Engineering
MIT Manipal

GitHub:
https://github.com/ashishh0555

Built using Streamlit and Stability AI.
