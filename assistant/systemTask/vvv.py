import os
import speech_recognition as sr
import pyttsx3
import pyautogui
import time

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def find_video_file(root_folder, file_name):
    file_name = file_name.lower().strip()
    if not file_name.endswith('.mp4'):
        file_name += '.mp4'

    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.lower() == file_name:
                print(f"File found: {os.path.join(root, file)}")
                return os.path.join(root, file)
    print("File not found")
    return None

def listen_for_commands(recognizer, microphone):
    while True:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Command heard: {command}")

            if "stop" in command or "pause" in command:
                pyautogui.press('space')
            elif "play" in command or "start" in command:
                pyautogui.press('space')
            elif "increase volume" in command or "volume up" in command:
                for _ in range(5):
                    pyautogui.press('volumeup')
            elif "decrease volume" in command or "volume down" in command or "drop the volume" in command:
                for _ in range(5):
                    pyautogui.press('volumedown')
            elif "exit" in command:
                speak("Exiting video player.")
                break

        except sr.UnknownValueError:
            speak("Sorry, I did not understand. Please repeat.")
        except sr.RequestError:
            speak("Service is down")

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        speak("What is the name of the video file ")
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            video_name = recognizer.recognize_google(audio).lower()
            if video_name == "exit":
                speak("Exiting application.")
                break

            video_path = find_video_file("D:\Video", video_name)

            if video_path:
                speak(f"Opening {video_name}")
                os.startfile(video_path)
                time.sleep(1)
                listen_for_commands(recognizer, microphone)
                break
            else:
                speak("Video file not found, please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I could not understand the video name. Please say it again.")
        except sr.RequestError:
            speak("Failed to get the response from Google. Please check your internet connection.")

if __name__ == "__main__":
    main()
