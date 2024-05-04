from setup.listen import listen
from setup.speak import speak
from systemTask import cal,minmax,note,ss
from helper import api
import tkinter as tk
from tkinter import scrolledtext
import threading

app = tk.Tk()
app.title("AI Assistant")
app.geometry("800x600")
output_text = scrolledtext.ScrolledText(app, wrap=tk.WORD)
output_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


def process_command():
    global listening
    speak("hello sir i am your bot please tell me how can i helo you")
    while listening:
        user = listen(output_text)
        intent = api.get_intent(user)
        print(intent)
        if user == "quit":
            q=False


listening = False
command_thread = threading.Thread(target=process_command)
def toggle_listening():
    global listening
    if not listening:
        listening = True
        start_button.config(text="Stop Listening", command=toggle_listening)
        output_text.insert(tk.END, "AI Assistant is listening...\n")
        speak("AI Assistant is listening")
        command_thread.start()
    else:
        listening = False
        start_button.config(text="Start Listening", command=toggle_listening)
        output_text.insert(tk.END, "AI Assistant has stopped listening.\n")
start_button = tk.Button(app, text="Start Listening", command=toggle_listening)
start_button.pack()
app.mainloop()
