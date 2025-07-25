import os
import time
import speech_recognition as sr
from dotenv import load_dotenv
from groq import Groq
import simpleaudio as sa  

#.env file
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found")
client = Groq(api_key=GROQ_API_KEY)

def record_audio(filename="input.wav"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak now... (max 10s, will stop if silent)")
        audio = recognizer.listen(source, timeout=3, phrase_time_limit=10)
        print("✅ Audio recorded.")
        with open(filename, "wb") as f:
            f.write(audio.get_wav_data())
    return filename


def transcribe_audio(file_path):
    with open(file_path, "rb") as f:
        transcription = client.audio.transcriptions.create(
            file=f,
            model="whisper-large-v3-turbo",
            language="en",
            temperature=0.0
        )
    return transcription.text.strip()

def get_groq_response(prompt):
    chat = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "Keep responses short and under 3 sentences."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return chat.choices[0].message.content.strip()

def text_to_speech(text, output_path="speech.wav"):
    response = client.audio.speech.create(
        model="playai-tts",
        voice="Fritz-PlayAI",
        input=text,
        response_format="wav"
    )
    response.write_to_file(output_path)
    return output_path

def play_audio(path):
    wave_obj = sa.WaveObject.from_wave_file(path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def main():
    print("🤖 Voice Assistant (Groq powered)\n")
    
    try:
        audio_file = record_audio()
        transcribed = transcribe_audio(audio_file)
        print(f"📝 You said: {transcribed}")
        
        if transcribed and len(transcribed.strip()) >= 2:
            reply = get_groq_response(transcribed)
            print(f"🤖 Assistant: {reply}")
            try:
                speech_path = text_to_speech(reply)
                play_audio(speech_path)
            except Exception as tts_error:
                print(f"⚠️ TTS Error: {tts_error}")
        else:
            print("⚠️ Didn't catch that. Please speak clearly.")
            
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    while True:
        main()
        cont = input("▶️ Ask again? (y/n): ").strip().lower()
        if cont != "y":
            print("👋 Goodbye!")
            break
