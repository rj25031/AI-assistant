import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext


def listen(output_text):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        output_text.insert(tk.END, "Listening...\n")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")  
        output_text.insert(tk.END, "Recognizing...\n")
        query =recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        output_text.insert(tk.END, f"User said: {query}\n")


    except Exception as e: 
        print("Didnt Get That Say that again please...\n")  
        output_text.insert(tk.END, "Didnt Get That Say that again please...\n")

        return "None"
    return query