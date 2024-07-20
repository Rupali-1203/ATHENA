# ATHENA Virtual Assistant
## _Developed by Rupali Susar Patil_

ATHENA is an advanced virtual assistant designed to streamline everyday tasks through voice commands. It leverages state-of-the-art natural language processing (NLP) techniques to provide accurate and quick responses.

## Features:
- **Voice Command Recognition:** Uses Google's speech recognition to process voice commands.
- **Natural Language Processing:** Employs Hugging Face transformers for AI command processing.
- **Web Browsing:** Opens popular websites like Google, Facebook, YouTube, and LinkedIn.
- **Music Playback:** Integrates with a music library to play songs.
- **News Updates:** Fetches top news headlines using the NewsAPI.

## Tech Stack:
- **Speech Recognition:** `speech_recognition`
- **Text-to-Speech:** `pyttsx3`
- **Web Browsing:** `webbrowser`
- **API Requests:** `requests`
- **NLP:** Hugging Face transformers with `gpt-2`
- **Fuzzy String Matching:** `fuzzywuzzy`

## Getting Started

### 1. Clone the Repository:

```sh
git clone https://github.com/Rupali-1203/ATHENA.git
cd ATHENA
```

### 2. Create and Activate Virtual Environment:
```sh
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
```

### 3. Install Dependencies:
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables:
Create a `.env` file in the root directory and add your NewsAPI key:
```sh
NEWS_API_KEY=your_api_key_here
```

### 5. Run ATHENA:
```sh
python main.py
```

## How It Works:
ATHENA listens for the wake word "ATHENA" and responds to various voice commands:
- **Opening Websites:** "Open Google", "Open Facebook", etc.
- **Playing Music:** "Play [song name]"
- **Fetching News:** "News"

ATHENA processes commands using Hugging Face's GPT-2 model and converts text to speech for responses.



## Team Members
[![LinkedIn](https://img.shields.io/badge/LINKEDIN-RUPALI%20SUSARPATIL-blue)](https://www.linkedin.com/in/rupali-susar-patil-86b297228/)

## Acknowledgments:
- A big thank you to the open-source community and developers of the libraries used in this project.
