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

