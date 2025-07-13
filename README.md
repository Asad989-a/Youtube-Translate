# 🎥 AI Agents: YouTube Summary + Spanish Translator

This Hugging Face app allows users to input any YouTube video URL, get an instant AI-generated **English summary**, and an automatic **Spanish translation** — all powered by collaborating AI agents.

---

## 🚀 Live App

👉 [Try the App on Hugging Face](https://huggingface.co/spaces/asad231/Lead-with-ai-agents)

---

## 🧠 How It Works

This project uses a multi-agent simulation:

- **Agent 1: Summarizer**  
  Parses the YouTube video (based on its ID) and provides a simulated summary.

- **Agent 2: Translator**  
  Automatically translates the summary into **Spanish** using `deep_translator`.

- **Master Agent**  
  Orchestrates both agents and displays the result, along with an embedded YouTube preview.

---

## 📦 Tech Stack

- 🐍 Python 3.10+
- 🤖 [Gradio](https://www.gradio.app/) for the interface
- 🌍 [deep-translator](https://pypi.org/project/deep-translator/) for translation
- 🎥 YouTube video ID extraction via `re`
- 🧠 Simulated AI agent behavior

---

## 📁 Folder Structure

ai-youtube-translator/
├── app.py # Main Gradio app
├── requirements.txt # Dependencies
└── README.md # You're reading this

yaml
Copy
Edit

---

## 📋 Example Video IDs

You can test the app using:

- `https://www.youtube.com/shorts/L7rnto5Oe0s?feature=share`
- `https://www.youtube.com/shorts/-mMbOxXNPhY?feature=share`
- `https://www.youtube.com/shorts/bUbV2CIHHmU?feature=share`

The app embeds the video and shows the summary + Spanish translation.

---

## 🌐 Future Scope

- 🧠 Real YouTube Transcript + Whisper support
- 🌍 Add support for more languages (Urdu, French, etc.)
- 📥 Downloadable summaries
- 🧾 Summarization for long-form YouTube videos
- 🧩 Chrome Extension for live translation

---

## 💡 Bonus Features

✅ Built with GenAI Hackathon Challenge in mind  
✅ Hugging Face deployment ready  
✅ No YouTube API key needed  
✅ Fully open-source

---

## 🛠️ Installation (Optional for Local)

```bash
pip install -r requirements.txt
python app.py

title: Lead With Ai Agents
emoji: 🌍
colorFrom: gray
colorTo: blue
sdk: gradio
sdk_version: 5.36.2
app_file: app.py
pinned: false

