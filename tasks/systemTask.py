import pyautogui

def screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
