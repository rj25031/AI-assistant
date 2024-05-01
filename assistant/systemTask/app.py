import speech_recognition as sr
import subprocess
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    """Function to speak a given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to listen to user's voice command and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

def find_application_path(app_name):
    """Function to find an application path using the 'where' command."""
    try:
        # Normalize the application name to include '.exe' if not already present
        if not app_name.lower().endswith(".exe"):
            app_name += ".exe"
        
        # Using 'where' command to find the application
        result = subprocess.run(["where", app_name], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.splitlines()[0]  # Return the first match
        else:
            return None
    except Exception as e:
        print(f"Error finding application: {str(e)}")
        return None

def open_application(app_name):
    """Function to open an application."""
    app_path = find_application_path(app_name)
    if app_path:
        subprocess.Popen([app_path], shell=True)
        speak(f"Opening {app_name}")
    else:
        speak("Application not found. Please try again.")

def main():
    speak("Which application would you like to open?")
    app_name = listen()
    if app_name:
        open_application(app_name)

if __name__ == "__main__":
    main()
