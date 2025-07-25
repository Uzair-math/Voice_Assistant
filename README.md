# 🎙️ Voice Assistant with Groq AI

This is a simple Python-based voice assistant that listens to human speech, converts it into text, sends the query to an AI model via the Groq API, and reads out the response using audio playback.

---

## 🚀 Features

- 🎤 Converts human voice to text
- 🧠 Sends text to Groq API for AI-generated responses
- 🔊 Plays AI responses using `simpleaudio`
- 🔐 API key and model configurations managed in `config.py`

---

## 🛠️ Technologies Used

- Python
- Groq API (Chat Completion Endpoint)
- `speech_recognition` (for voice input)
- `simpleaudio` (for audio playback)
- `pyttsx3` or `gTTS` (for text-to-speech, if included)
- `config.py` for secure API key management

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/voice-assistant.git
   cd voice-assistant
   pip install -r requirements.txt
GROQ_API_KEY = "your-groq-api-key"
GROQ_MODEL = "llama3-8b-8192"  # or any model you're using


python main.py

(venv) PS D:\Data\Practice\voice_assistent-main> python main.py
🤖 Voice Assistant (Groq powered)

🎙️ Speak now... (max 10s, will stop if silent)
✅ Audio recorded.
📝 You said: Now what time is now Pakistan in?
🤖 Assistant: Pakistan is in Pakistan Standard Time (PST), which is UTC+5.
⚠️ TTS Error: Error code: 400 - {'error': {'message': 'The model `playai-tts` requires terms acceptance. Please have the org admin accept the terms at https://console.groq.com/playground?m
odel=playai-tts', 'type': 'invalid_request_error', 'code': 'model_terms_required'}}
▶️ Ask again? (y/n): y
🤖 Voice Assistant (Groq powered)

🎙️ Speak now... (max 10s, will stop if silent)
✅ Audio recorded.
📝 You said: Now where London time is
🤖 Assistant: You want to know the current time in London! As of now, the current time in London is [insert current time in London].
⚠️ TTS Error: Error code: 400 - {'error': {'message': 'The model `playai-tts` requires terms acceptance. Please have the org admin accept the terms at https://console.groq.com/playground?m
odel=playai-tts', 'type': 'invalid_request_error', 'code': 'model_terms_required'}}
▶️ Ask again? (y/n): n
👋 Goodbye!
(venv) PS D:\Data\Practice\voice_assistent-main> 
