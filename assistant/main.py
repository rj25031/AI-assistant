from setup.listen import listen
from setup.speak import speak
from systemTask import cal,minmax,ss,ar,vvv,application,weather,shutdown,send_email
from webTask import webTask
from helper import api
import tkinter as tk
from tkinter import scrolledtext
import threading

app = tk.Tk()
app.title("AI Assistant")
app.geometry("400x600")
output_text = scrolledtext.ScrolledText(app, wrap=tk.WORD)
output_text.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)


def process_command():
    global listening
    speak("hello sir i am your bot please tell me how can i help you")
    while listening:
        user = listen(output_text)
        intent,response,entity = api.get_intent(user)
        print(entity)
        print(intent)

        if intent == "take_ss":
            speak(response)
            output_text.insert(tk.END,response+"\n")
            res = ss.take_screenshot()
            output_text.insert(tk.END,res+"\n")
            speak(res)
        elif intent == "calculate":
            result = cal.match_math_expression(user)
            if result:
                output_text.insert(tk.END, "the result of this calculation is" + str(result)+"\n")
                speak("the result of this calculation is" + str(result)+"\n")
            else:
                output_text.insert(tk.END, "did not get the expression please tell again\n")
                speak("did not get the expression please tell again\n")
        elif intent == "play_video":
            title = entity['video_subject']
            vvv.playing_video(title)
            speak("playing"+title)
            output_text.insert(tk.END,"playing"+title+"\n")
        elif intent == "web_search":
            webTask.web_search(entity['query'])
            webTask.read_description(entity['query'])
        elif intent == "set_reminder":
            msg = ar.set_up_reminder(entity["task"],entity["time"])
            speak(msg)
            output_text.insert(tk.END,msg+"\n")
        elif intent == "open_app":
            res = application.open_application(entity["app"])
            speak(res)
            output_text.insert(tk.END,res+"\n") 
        elif intent == "get_weather":
            city = entity["city"]
            weather_info = weather.get_weather(city)
            speak(weather_info["temperature"])
            speak(weather_info["humidity"])
            speak(weather_info[ "wind_speed"])
            output_text.insert(tk.END , weather_info["temperature"])
            output_text.insert(tk.END , weather_info["humidity"])
            output_text.insert(tk.END , weather_info[ "wind_speed"])
        elif intent == "play_music":
           vvv.playing_music(entity["song"])
        elif intent == "media_action":
            vvv.control_youtube(entity["action"])
        elif intent == "shutdown_computer":
            shutdown.perform_action("shutdown")
        elif intent == "restart_computer":
            shutdown.perform_action("restart")
        elif intent == "minimize_window":
            minmax.minimize_window()
        elif intent == "maximize_window":
            minmax.maximize_window()
        elif intent == "email":
            speak("what is the email id of the receiver")
            email = listen(output_text).replace(" ","")+"@gmail.com"
            print(email)
            speak("what is the subject")
            sub = listen(output_text)
            speak("what is the message to send")
            body = listen(output_text)
            res = send_email.send_email(email.lower(),sub,body)
            speak(res)
            output_text.insert(tk.END ,res+"\n")


listening = False
def toggle_listening():
    global listening
    if not listening:
        listening = True
        start_button.config(text="Stop Listening", command=toggle_listening)
        output_text.insert(tk.END, "AI Assistant is listening...\n")
        speak("AI Assistant is listening")
        command_thread = threading.Thread(target=process_command)
        command_thread.start()
    else:
        listening = False
        start_button.config(text="Start Listening", command=toggle_listening)
        output_text.insert(tk.END, "AI Assistant has stopped listening.\n")

start_button = tk.Button(app,  borderwidth=5, relief='raised', foreground='black', background='#4CAF50', text="Start Listening", command=toggle_listening)
start_button.pack()
app.mainloop()
