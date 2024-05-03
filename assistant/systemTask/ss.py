import os
import pyautogui
import speech_recognition as sr

def take_screenshot():
    # Create the screenshots directory if it doesn't exist
    directory = 'screenshots'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate a unique filename for the screenshot
    screenshot_name = os.path.join(directory, f'screenshot_{len(os.listdir(directory)) + 1}.png')

    # Take the screenshot and save it
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_name)
    print(f"Screenshot saved as {screenshot_name}")

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
        if "screenshot" in command:
            take_screenshot()
        elif "exit" in command:
            print("Exiting...")
            break
