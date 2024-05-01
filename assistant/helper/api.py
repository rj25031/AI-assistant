import requests

def get_intent(message):
    url = "http://localhost:5005/model/parse"
    data = {
        "text": message
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        parsed_response = response.json()
        intent = parsed_response["intent"]["name"]
        return intent
        # return parsed_response
    except requests.exceptions.RequestException as e:
        print("Error making request:", e)
        return None

