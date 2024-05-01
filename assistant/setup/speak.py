import pyttsx3

def speak(text):
    
    engine = pyttsx3.init()

    engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

    engine.say(text)

    engine.runAndWait()
