import os
import subprocess
import speech_recognition as sr
import pyttsx3

def open_notepad():
    subprocess.Popen(["notepad.exe"])

def take_note():
    print("Speak your note:")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        note = recognizer.recognize_google(audio)
        return note
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def save_note(note, filename):
    notes_folder = "notes"
    if not os.path.exists(notes_folder):
        os.makedirs(notes_folder)
    with open(os.path.join(notes_folder, filename), 'w') as file:
        file.write(note)
    print(f"Note saved as '{filename}' successfully!!!")

def read_note(filename):
    try:
        with open(os.path.join("notes", filename), 'r') as file:
            note = file.read()
            speak(note)
    except FileNotFoundError:
        print("Note file not found.")

def delete_note(filename):
    try:
        os.remove(os.path.join("notes", filename))
        print(f"Note '{filename}' deleted successfully!!!")
    except FileNotFoundError:
        print("Note file not found.")

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

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        command = listen()
        if "open notepad" in command:
            open_notepad()
        elif "take a note" in command:
            note = take_note()
            if note:
                print("Do you want to save this note? (yes/no)")
                choice = input().lower()
                if choice == "yes":
                    print("Enter a name for this note:")
                    filename = input() + ".txt"
                    save_note(note, filename)
        elif "read note" in command:
            print("Enter the name of the note you want to read:")
            filename = input() + ".txt"
            read_note(filename)
        elif "delete note" in command:
            print("Enter the name of the note you want to delete:")
            filename = input() + ".txt"
            delete_note(filename)
        elif "exit" in command:
            print("Exiting...")
            break
