import win32gui

def minimize_window():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, 6)

def maximize_window():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, 3)