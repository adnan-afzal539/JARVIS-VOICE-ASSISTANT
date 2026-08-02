import speech_recognition as sr
import webbrowser
from gtts import gTTS
from time import time
import songsLibrairy
import requests
from google import genai
from dotenv import load_dotenv

import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame
pygame.mixer.init()


load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")



def speak(text):

    filename = f"voice_{int(time())}.mp3"

    tts = gTTS(text)
    tts.save(filename)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()

    os.remove(filename)


def get_news():

    speak("Here are todays top news")

    api_key = NEWS_API_KEY

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    response = requests.get(url)
    data = response.json()

    for article in data["articles"][:5]:
        speak(article["title"])




api = GEMINI_API_KEY
client = genai.Client(api_key = api)
def ask_ai(problem):

    prompt = f"""You are an AI assistant named Jarvis dont 
    answer the questions in very much lines
      and behave like a voice assistant
      Question ; {problem}"""


    response = client.models.generate_content(
        model= "gemini-3.1-flash-lite",

        contents= prompt
    )

    speak(response.text)




def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        music = c.lower().replace("play","").strip()
        link = songsLibrairy.songs[music]
        webbrowser.open(link)

    elif "sherry" in c.lower() or "hammad" in c.lower():
        speak("They are great man no one can dare tallk  regarding them my love")

    elif "news" in c.lower():
        get_news()

    else:
        ask_ai(c)



if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake word Jarvis
        # Obtain audio from the microphone
        r = sr.Recognizer()
        

        print("recognizing")

        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            print("wake word: ", word)


            if word.lower() == "jarvis":
                speak("Ya")



                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active....")
                    audio = r.listen(source, timeout=2, phrase_time_limit=15)
                command = r.recognize_google(audio)
                print("command", command)

                processCommand(command)

        except Exception as e:
            print(type(e).__name__)
            print(e)