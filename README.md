# 🤖 JARVIS Task Assistant

JARVIS is your intelligent voice-based personal assistant designed to perform system tasks, respond to queries, and manage communication using **LLM-powered reasoning** and **real-time voice commands**. Inspired by Iron Man's JARVIS, this assistant brings automation and conversation to your desktop.

---

## 🚀 Features

- 🎙️ Voice Interaction using Speech Recognition
- 🧠 LLM-based Reasoning with Dual Agents (Logical + Tone-aware)
- 🧾 Natural Language Understanding
- 🧬 Multi-layered Processing with RAG (Retrieval-Augmented Generation)
- 🕹️ Open local applications or web pages
- 📞 Make Phone Calls or Send SMS/WhatsApp
- 🎵 Play Songs on YouTube
- ⏰ Get System Time and Custom Replies
- 🗣️ Friendly and Adaptive Conversational Flow
- 📁 SQLite-based Local Command and Contact Database

---

## 🧠 Architecture Overview
User → Voice Command/Text → JARVIS Engine
→ Command Handler → Feature Executor
→ If Chat → Reasoning Agent → Response Agent → Output


---

## 📦 Tech Stack

| Component        | Technology                         |
|------------------|-------------------------------------|
| Voice Input      | `speech_recognition`, `pyttsx3`     |
| UI Engine        | `Streamlit`                         |
| Audio Playback   | `playsound`                         |
| Automation       | `pyautogui`, `os`, `webbrowser`     |
| Database         | `SQLite3`                           |
| NLP / Chat       | `OpenAI/OpenRouter` via RAG agents  |
| Media            | `pywhatkit` for YouTube             |
| Mobile Control   | `ADB` commands for calls & SMS      |

---

## 🛠️ Setup Instructions

### 1. 📥 Install Requirements

pip install streamlit pyttsx3 speechrecognition pyautogui pywhatkit playsound openai

