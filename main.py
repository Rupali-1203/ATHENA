import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import musiclibrary
import os
from dotenv import load_dotenv
from transformers import pipeline

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize Hugging Face text generation pipeline with PyTorch support
generator = pipeline('text-generation', model='gpt2')  # Ensure PyTorch is installed

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process AI commands using Hugging Face API
def aiProcess(command):
    response = generator(command, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']

# Function to process various commands
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={NEWS_API_KEY}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:5]:  # Limit to first 5 articles
                speak(article['title'])
    else:
        output = aiProcess(c)
        speak(output)

# Main loop to listen for commands
if __name__ == "__main__":
    speak("Initializing ATHENA... ")
    while True:
        try:
            with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                print("Listening for 'ATHENA'...")

                # Listen for the wake word "ATHENA"
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=1)
                word = recognizer.recognize_google(audio)

                if word.lower() == "athena":
                    speak("Yes")
                    
                    # Listen for the actual command
                    print("ATHENA is active, listening for command...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    # Process the command
                    processCommand(command)
                elif word.lower()!= "athena":
                    speak("wrong pronounciation")
        
        

        except Exception as e:
            print(f"Error: {e}")
