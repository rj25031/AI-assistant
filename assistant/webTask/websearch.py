import webbrowser
import pyttsx3
import requests
from bs4 import BeautifulSoup

def web_search(query):
    try:
        # Construct the Google search URL
        search_url = f"https://www.google.com/search?q={query}"

        # Open the search URL in the default web browser
        webbrowser.open(search_url)

    except Exception as e:
        print("An error occurred:", str(e))

def read_description(query):
    try:
        # Construct the Google search URL
        search_url = f"https://www.google.com/search?q={query}"

        # Send a request to Google search and parse the HTML response
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the description element
        description_tag = soup.find('div', class_='BNeawe s3v9rd AP7Wnd')

        # Extract the text from the description element
        description_text = description_tag.text.strip() if description_tag else "No description found."

        # Initialize pyttsx3
        engine = pyttsx3.init()

        # Speak the description
        engine.say(description_text)
        engine.runAndWait()

    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
query = input("Enter your search query: ")
web_search(query)
read_description(query)