import asyncio
from rasa.core.agent import Agent
import speech_recognition as sr
import pyttsx3
import logging

# Set logging level to ERROR to suppress debug logs
logging.getLogger('rasa').setLevel(logging.ERROR)
def speak(text):
    
    engine = pyttsx3.init()

    engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

    engine.say(text)

    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception as e:
        print(e)
        return ""

interpreter = Agent.load("D:/MP/assistant/assistant/brain/models/20240417-180022-gray-anchovy.tar.gz")

async def handle_input():
    q=True
    speak("hello i am bot please tell me how can i help you")
    while q:
        # user_input = input('user:')
        user_input = listen()
        if 'quit' in user_input:
            q=False

        responses = await interpreter.handle_text(user_input)

        for response in responses:

            print("Bot:", response.get("text"))
            speak(response.get("text"))

            intent = response.get("intent").get("name")
            entities = response.get("entities")
            print(intent,entities)

asyncio.run(handle_input())
