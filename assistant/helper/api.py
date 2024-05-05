import requests

def get_intent(message):
    url = "http://localhost:5005/model/parse"
    data = {
        "text": message
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  
        parsed_response = response.json()
        intent = parsed_response["intent"]["name"]
        response_text = parsed_response.get("response", "") 
        
        # Extract entities
        entities = parsed_response.get("entities", [])
        extracted_entities = {}
        for entity in entities:
            entity_type = entity["entity"]
            entity_value = entity["value"]
            extracted_entities[entity_type] = entity_value
        
        return intent, response_text, extracted_entities
    except requests.exceptions.RequestException as e:
        print("Error making request:", e)
        return None, None, None
