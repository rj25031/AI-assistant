import webbrowser
import pyttsx3
import requests
from bs4 import BeautifulSoup

def web_search(query):
    try:
        search_url = f"https://www.google.com/search?q={query}"

        webbrowser.open(search_url)

    except Exception as e:
        print("An error occurred:", str(e))

def read_description(query):
    try:
        search_url = f"https://www.google.com/search?q={query}"

        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        description_tag = soup.find('div', class_='BNeawe s3v9rd AP7Wnd')

        description_text = description_tag.text.strip() if description_tag else "No description found."

        engine = pyttsx3.init()

        engine.say(description_text)
        engine.runAndWait()

    except Exception as e:
        print("An error occurred:", str(e))
