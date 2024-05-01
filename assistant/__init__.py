# import pyttsx3 
# import speech_recognition as sr 
# import datetime
# import wikipedia 
# import webbrowser
# import os
# import smtplib
# import pywhatkit
# import pyautogui
# import time
# import subprocess
# import psutil




# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()


# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=6 and hour<12:
#         speak("Good Morning!")
#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")  
#     elif hour>=18 and hour<20:
#         speak("Good Evening!")  
#     else:
#         speak("Good Night!")  

#     speak("I am Jarvis Sir. Please tell me how may I help you")    

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source, duration=1)
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")

#     except Exception as e: 
#         print("Say that again please...")  
#         return "None"
#     return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('pritannari@gmail.com', 'ugtophsrmkbbtwdu')
#     server.sendmail('pritannari@gmail.com', to, content)
#     server.close()

# if __name__ == "__main__":
#     wishMe()
#     q=True
#     while q:
#         print("say quit to quit")
#         query = takeCommand().lower()
#         if 'wikipedia' in query:
#             speak('Searching Wikipedia...')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=2)
#             speak("According to Wikipedia")
#             print(results)
#             speak(results)

#         elif 'play' in query:
#             if 'play music' in query:
#                 song_path = 'Daku-(PagalWorld.Ink).mp3'
#                 os.system("start " + song_path)
#             else:
#                 query = query.replace("play", "")
#                 pywhatkit.playonyt(query) 
#         elif 'pause' in query:
#             pyautogui.hotkey('space')
#         elif 'resume' in query: 
#             pyautogui.hotkey('space')
#         elif 'open ' in query:
#             webbrowser.open("google.com")
#         elif 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")    
#             speak(f"Sir, the time is {strTime}")
#         elif 'luanch code' in query:
#             codePath = "C:\\Users\\Rupesh Jadhav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#             os.startfile(codePath)

#         elif 'send a mail' in query:
#             try:
#                 speak('tell the adress of reicever')
#                 to= takeCommand()
#                 speak("What should I say?")
#                 content = takeCommand()
#                 to=to.replace(' ','')
#                 sendEmail(to, content)
#                 speak("Email has been sent!")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry . I am not able to send this email")    
#         elif 'quit' in query:
#             q=False
#         elif 'check system update' in query:
#             output = subprocess.check_output("wuauclt.exe /detectnow /updatenow", shell=True)
#             if b"New updates are available" in output:
#                 speak("Windows updates are available.")
#                 speak('whould you like to update the system ?')
#                 ans=takeCommand()
#                 if 'yes' in ans:
#                     return_code = subprocess.run(['powershell', 'Start-Process', 'cmd.exe', '/c', 'start', 'cmd.exe', '/k', 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', '-Command', 'Update-Help; Update-Module; Update-Script; Get-HotFix; choco upgrade all -y']).returncode
#                     if return_code == 0:
#                         speak("System update successful!")
#                     else:
#                         speak("System update failed!")
#             else:
#                  print("Windows is up to date.")
#         elif 'system status' in query:
#                 cpu_usage = psutil.cpu_percent()
#                 mem_usage = psutil.virtual_memory().percent
#                 disk_usage = psutil.disk_usage("/").percent
#                 speak("CPU usage:") 
#                 speak(cpu_usage)
#                 speak("%")
#                 print("CPU usage:", cpu_usage, "%")
#                 speak("Memory usage:") 
#                 speak(mem_usage)
#                 speak("%")
#                 print("Memory usage:", mem_usage, "%")
#                 speak("Disk usage:") 
#                 speak(disk_usage)
#                 speak("%")
#                 print("Disk usage:", disk_usage, "%")
#                 time.sleep(1)
#         elif 'search a file' in query:
#             speak('name the file you want to search with extention')
#             fi=takeCommand()
#             directory = "C:"
#             extension = "pass.txt"
#             for root, dirs, files in os.walk(directory):
#                 for file in files:
#                     if file.endswith(fi):
#                         os.open(os.path.join(root, file))
#         elif 'take a screenshot' in query:
#             screenshot = pyautogui.screenshot()
#             screenshot.save('screenshot.png')


