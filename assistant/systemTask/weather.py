import requests
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

def get_weather(city):
    api_key = "12dd1ef813fbc3be279a31f915dcc018"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "uv_index": "N/A",
            "air_quality_index": "N/A",
            "sunrise": data["sys"]["sunrise"],
            "sunset": data["sys"]["sunset"]
        }
        return weather
    else:
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Which city's weather do you want to know?")
    city = listen()
    weather = get_weather(city)
    if weather:
        speak("What updates would you like to know?")
        while True:
            command = listen()
            if "temperature" in command:
                speak(f"The current temperature in {city} is {weather['temperature']} degrees Celsius.")
            elif "humidity" in command:
                speak(f"The humidity in {city} is {weather['humidity']}%.")
            elif "wind speed" in command:
                speak(f"The wind speed in {city} is {weather['wind_speed']} meters per second.")
            elif "exit" in command:
                speak("Exiting...")
                print("Exiting...")
                break
            else:
                speak("Sorry, I couldn't understand that. Please ask for temperature, humidity, or wind speed.")
    else:
        speak(f"Sorry, I couldn't retrieve the weather data for {city}. Please try again later.")
