import speech_recognition as sr
import datetime
from playsound import playsound
import pyttsx3

# Initialize the recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to set a reminder
def set_reminder():
    try:
        # Listen for the date
        speak("When do you want to be reminded? (e.g., 'April 30, 2024')")
        with sr.Microphone() as source:
            audio = r.listen(source)
            date_str = r.recognize_google(audio)
            reminder_date = datetime.datetime.strptime(date_str, "%B %d, %Y")

        # Listen for the time
        speak("What time do you want to be reminded? (e.g., '3:30 PM')")
        with sr.Microphone() as source:
            audio = r.listen(source)
            time_str = r.recognize_google(audio)
            reminder_time = datetime.datetime.strptime(time_str, "%I:%M %p").time()

        # Listen for the reason
        speak("What's the reminder for?")
        with sr.Microphone() as source:
            audio = r.listen(source)
            reason = r.recognize_google(audio)

        # Set the reminder time
        reminder_datetime = datetime.datetime.combine(reminder_date.date(), reminder_time)
        speak(f"Reminder set for {reminder_datetime.strftime('%A, %B %d, %Y %I:%M %p')}: {reason}")

    except Exception as e:
        speak(f"Error: {e}")

# Function to set an alarm
def set_alarm():
    try:
        # Listen for the time
        speak("What time do you want to set the alarm for? (e.g., '6:00 AM', '1:00 PM', '6:00 PM')")
        with sr.Microphone() as source:
            audio = r.listen(source)
            time_str = r.recognize_google(audio)

        # Parse the time string and set the alarm time
        time_format = "%I:%M %p"
        try:
            alarm_time = datetime.datetime.strptime(time_str, time_format).time()
        except ValueError:
            speak(f"Error: Could not parse the time '{time_str}'. Please try again.")
            return

        speak(f"Alarm set for {alarm_time.strftime('%I:%M %p')}")

        # Play the alarm sound at the specified time
        while True:
            current_time = datetime.datetime.now().time()
            if current_time >= alarm_time:
                playsound("alarm_sound.mp3")
                break

    except Exception as e:
        speak(f"Error: {e}")

# Main function
def main():
    try:
        speak("Do you want to set a reminder or an alarm?")
        with sr.Microphone() as source:
            audio = r.listen(source)
            choice = r.recognize_google(audio)

        if "reminder" in choice:
            set_reminder()
        elif "alarm" in choice:
            set_alarm()
        else:
            speak("Invalid choice. Please try again.")

    except Exception as e:
        speak(f"Error: {e}")

if __name__ == "__main__":
    main()