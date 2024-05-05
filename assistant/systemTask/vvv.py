import pywhatkit
import pyautogui
import time

def playing_video(title):
    pywhatkit.playonyt(title)

def playing_music(title):
    pywhatkit.playonyt(title)

def control_youtube(action):
    if action == "stop":
        pyautogui.press('ctrl')
        pyautogui.press('space')  
    elif action == "resume":
        pyautogui.press('ctrl')
        pyautogui.press('space')  # Resume playback
    elif action == "volume_up":
        pyautogui.press('ctrl')
        pyautogui.press('up')     # Increase volume
    elif action == "volume_down":
        pyautogui.press('ctrl')
        pyautogui.press('down')   # Decrease volume
    elif action == "next":
        pyautogui.press('ctrl')
        pyautogui.press('right')  # Skip to next video
    elif action == "previous":
        pyautogui.press('ctrl')
        pyautogui.press('left')   # Go to previous video

