import pyautogui
import speech_recognition as sr
import win32gui

def minimize_window():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, 6)

def maximize_window():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, 3)

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

if __name__ == "__main__":
    while True:
        command = listen()
        if "minimise" in command:
            minimize_window()
            print("Window minimized.")
        elif "maximize" in command:
            maximize_window()
            print("Window maximized.")
        elif "exit" in command:
            print("Exiting...")
            break
