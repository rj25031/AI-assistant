import smtplib
from email.message import EmailMessage
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
            text = text.lower().replace("at the rate", "@").replace("dot", ".").replace(" ", "")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def send_email(to, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = "Ithe Tuzha mail tak lavdya"
    msg['To'] = to

    try:
        with smtplib.SMTP('smtp.gmail.com', 578) as server:
            server.starttls()
            server.login("yashdalvi23903@gmail.com", "")
            server.send_message(msg)
            print("Email sent successfully!")
            speak("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Failed to send the email.")

def main():
    speak("Who do you want to send the email to?")
    to = listen()
    if not to:
        speak("I didn't catch that, exiting.")
        return

    print(f"Formatted email address: {to}")

    speak("What is the subject of your email?")
    subject = listen()
    if not subject:
        speak("I didn't catch that, exiting.")
        return

    speak("What should the email say?")
    body = listen()
    if not body:
        speak("I didn't catch that, exiting.")
        return

    send_email(to, subject, body)

if _name_ == "_main_":
    main()