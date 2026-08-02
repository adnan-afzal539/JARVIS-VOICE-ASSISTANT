# Jarvis Voice Assistant


A voice-controlled AI assistant built with Python.

Jarvis can recognize voice commands, open websites, play music, read the latest news, and answer questions using Google's Gemini AI. It uses speech recognition, text-to-speech, and external APIs to provide a simple voice assistant experience.




## Features

- 🎤 Recognizes voice commands using SpeechRecognition
- 🌐 Opens websites such as Google, YouTube, Instagram, and LinkedIn
- 🎵 Plays songs from a predefined music library
- 📰 Reads the latest news using NewsAPI
- 🤖 Answers general questions using Google's Gemini AI
- 🔊 Speaks responses using Google Text-to-Speech (gTTS)



## Technologies Used

- Python
- SpeechRecognition
- gTTS (Google Text-to-Speech)
- Pygame
- Requests
- Google Gemini API
- NewsAPI



## Installation


1. Clone the repository

```bash
git clone https://github.com/adnan-afzal539/JARVIS-VOICE-ASSISTANT.git
```

2. Navigate to the project folder

```bash
cd JARVIS-VOICE-ASSISTANT
```

3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the virtual environment (Windows)

```bash
venv\Scripts\activate
```

5. Install the required packages

```bash
pip install -r requirements.txt
```

6. Create a `.env` file and add your API keys

```text
NEWS_API_KEY=your_news_api_key
GEMINI_API_KEY=your_gemini_api_key
```
Replace `your_news_api_key` and `your_gemini_api_key` with your actual API keys.

7. Run the project

```bash
python main.py
```



## Usage

1. Run the application.

```bash
python main.py
```

2. Say the wake word:

```text
Jarvis
```

3. Speak a command, for example:

```text
Open Google
Play Believer
What's the news?
Open YouTube
```



## Future Improvements

- Add support for more voice commands.
- Improve the AI conversation experience.
- Add a graphical user interface (GUI).
- Support multiple languages.
- Add system control commands (volume, applications, etc.).



## Author

GitHub: **Adnan Afzal**

https://github.com/adnan-afzal539