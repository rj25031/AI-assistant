from setup.listen import listen
from setup.speak import speak
from systemTask import cal,minmax,note,ss
from helper import api

q=True
speak("hello sir i am your bot please tell me how can i helo you")
while q:
    user = listen()
    intent = api.get_intent(user)
    print(intent)
    if user == "quit":
        q=False

