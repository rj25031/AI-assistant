from setup import speak,listen
from tasks import systemTask,webTask


query=listen.listen()


if "Wikipedia" in query:
    result = webTask.searchWikipedia(query)

    speak.speak(result)




