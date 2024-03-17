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

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"Error occurred during calculation: {e}")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        command = listen()
        if "exit" in command:
            speak("Exiting...")
            print("Exiting...")
            break
        elif any(op in command for op in ["add", "plus", "+", "sum"]):
            expression = command.replace("add", "+").replace("plus", "+").replace("sum", "+")
            result = calculate(expression)
            if result is not None:
                speak(f"The result is {result}")
                print(f"Result: {result}")
        elif any(op in command for op in ["subtract", "minus", "-", "difference"]):
            expression = command.replace("subtract", "-").replace("minus", "-").replace("difference", "-")
            result = calculate(expression)
            if result is not None:
                speak(f"The result is {result}")
                print(f"Result: {result}")
        elif any(op in command for op in ["multiply by", "times", "*", "product"]):
            expression = command.replace("multiply by", "*").replace("times", "*").replace("product", "*")
            result = calculate(expression)
            if result is not None:
                speak(f"The result is {result}")
                print(f"Result: {result}")
        elif any(op in command for op in ["divide", "divided by", "/", "quotient"]):
            expression = command.replace("divide", "/").replace("divided by", "/").replace("quotient", "/")
            result = calculate(expression)
            if result is not None:
                speak(f"The result is {result}")
                print(f"Result: {result}")
        else:
            speak("Command not recognized. Please try again.")
            print("Command not recognized. Please try again.")
