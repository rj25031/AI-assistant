import os
import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}\n")
        return command.lower()
    except Exception as e:
        print(e)
        return ""

def confirm_action(action):
    speak(f"Are you sure you want to {action} the desktop? Say yes to confirm.")
    confirmation = listen()
    return "yes" in confirmation

def perform_action(action):
    if action == "shutdown":
        os.system("shutdown /s /t 1")
    elif action == "restart":
        os.system("shutdown /r /t 1")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("What action would you like to perform? Shutdown or restart?")
    while True:
        command = listen()
        if "shutdown" in command:
            if confirm_action("shutdown"):
                perform_action("shutdown")
                break
        elif "restart" in command:
            if confirm_action("restart"):
                perform_action("restart")
                break
        else:
            speak("Sorry, I didn't get that. Please say 'shutdown' or 'restart'.")
