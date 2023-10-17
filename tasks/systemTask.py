import pyautogui
import wikipedia


def screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

