import os
import pyautogui

def take_screenshot():
    directory = 'screenshots'
    if not os.path.exists(directory):
        os.makedirs(directory)

    screenshot_name = os.path.join(directory, f'screenshot_{len(os.listdir(directory)) + 1}.png')

    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_name)
    return f"Screenshot saved as {screenshot_name}"


