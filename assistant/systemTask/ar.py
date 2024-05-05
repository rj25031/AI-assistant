from datetime import datetime
from win10toast import ToastNotifier
import threading

def notify_user(reminder_msg):
    toaster = ToastNotifier()
    toaster.show_toast("Reminder", reminder_msg, duration=10)

def set_up_reminder(task, time_str):
    reminder_time = datetime.strptime(time_str, '%I:%M %p')
    current_date = datetime.now().date()
    reminder_time = datetime.combine(current_date, reminder_time.time())
    current_time = datetime.now()
    time_diff = reminder_time - current_time
    if time_diff.total_seconds() < 0:
        return "Error: Reminder time is in the past."

    def background_reminder():
        import time
        time.sleep(time_diff.total_seconds())
        notify_user(task)

    threading.Thread(target=background_reminder).start()

    return f"Reminder set for {reminder_time.strftime('%I:%M %p')} today: {task}"
