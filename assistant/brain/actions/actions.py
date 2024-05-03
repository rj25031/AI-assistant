# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os
import pyautogui




class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"
    
    def take_screenshot(self):
        # Create the screenshots directory if it doesn't exist
        directory = 'screenshots'
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Generate a unique filename for the screenshot
        screenshot_name = os.path.join(directory, f'screenshot_{len(os.listdir(directory)) + 1}.png')

        # Take the screenshot and save it
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_name)
        return f"Screenshot saved as {screenshot_name}"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        ss = self.take_screenshot()
        dispatcher.utter_message(ss)

        return []
    
    
