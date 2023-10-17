import wikipedia 
import sys

def searchWikipedia(query):
    
    query.replace("wikipedia", "")

    try:
        wikipedia.set_lang('en')
        summary = wikipedia.summary(query,sentences=3)

        return summary
        
    except wikipedia.exceptions.DisambiguationError as e:
        return "Disambiguation Error", e.options
    except wikipedia.exceptions.PageError as e:
        return "Page Not Found", str(e)







