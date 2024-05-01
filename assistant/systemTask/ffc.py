import os
import re
import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen(prompt):
    print(prompt)  # Visual feedback in the console for debugging
    speak(prompt)
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        response = recognizer.recognize_google(audio)
        print(f"Recognized: {response}")
        return response
    except sr.UnknownValueError:
        return listen("I couldn't understand that. Please repeat.")
    except sr.RequestError:
        return listen("Failed to get response, please try again.")
    except sr.WaitTimeoutError:
        return listen("No response received, please speak again.")

def confirm_action(prompt):
    response = listen(prompt)
    if 'yes' in response.lower():
        return True
    elif 'no' in response.lower():
        return False
    else:
        return confirm_action("Please say yes or no.")

def parse_drive(input_str):
    """Convert commonly misinterpreted phrases to the correct drive letter."""
    match = re.search(r'\b([cde])\s*drive', input_str, re.IGNORECASE)
    if match:
        return match.group(1).upper()
    else:
        misinterpretations = {'sea': 'C', 'see': 'C'}
        for key in misinterpretations:
            if key in input_str.lower():
                return misinterpretations[key]
        return None

def delete_folder_or_file(path):
    """Delete a folder or file with confirmation."""
    if os.path.exists(path):
        if confirm_action(f"Are you sure you want to delete {os.path.basename(path)}? Please say yes or no."):
            if os.path.isdir(path):
                os.rmdir(path)
            else:
                os.remove(path)
            speak(f"{os.path.basename(path)} has been deleted successfully.")
        else:
            speak("Deletion cancelled.")
    else:
        speak("The specified path does not exist.")

def process_create_folder_options(full_path):
    option = listen("Would you like to create a new file or a new folder inside? Say 'file', 'folder', or 'done'.")
    if 'file' in option.lower():
        file_name = listen("What is the name of the file? Please include the file extension.")
        file_path = os.path.join(full_path, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write('')
            speak(f"File '{file_name}' created successfully.")
        else:
            speak("File already exists.")
        process_create_folder_options(full_path)
    elif 'folder' in option.lower():
        subfolder_name = listen("What is the name of the new folder?")
        subfolder_path = os.path.join(full_path, subfolder_name)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
            speak(f"Folder '{subfolder_name}' created successfully inside {os.path.basename(full_path)}.")
        else:
            speak("Folder already exists.")
        process_create_folder_options(full_path)
    elif 'done' in option.lower():
        speak("Alright, done with this folder.")

def process_create_folder():
    drive_response = listen("Which drive do you want to create a new folder in?")
    drive_letter = parse_drive(drive_response)
    if drive_letter and drive_letter in "CDE":
        folder_name = listen("What should be the name of the folder?")
        path = f"{drive_letter}:/"
        full_path = os.path.join(path, folder_name)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            speak(f"Folder '{folder_name}' created successfully in {drive_letter} drive.")
            process_create_folder_options(full_path)
        else:
            speak(f"Folder already exists in {drive_letter} drive.")

def process_delete_folder():
    drive_response = listen("In which drive is the folder you want to delete?")
    drive_letter = parse_drive(drive_response)
    if drive_letter and drive_letter in "CDE":
        folder_name = listen("What is the name of the folder you want to delete?")
        path = f"{drive_letter}:/"
        folder_path = os.path.join(path, folder_name)
        if os.path.exists(folder_path):
            delete_folder_or_file(folder_path)
        else:
            speak("The specified folder does not exist.")
    else:
        speak("Please specify a valid drive like 'C drive' or 'D drive'.")

def process_user_choice():
    choice = listen("Listening...")
    if 'create a file' in choice.lower():
        process_create_file()
    elif 'create a folder' in choice.lower():
        process_create_folder()
    elif 'delete a file' in choice.lower():
        process_delete_file()
    elif 'delete a folder' in choice.lower():
        process_delete_folder()
    elif 'exit' in choice.lower():
        speak("Exiting.")
        return False
    else:
        speak("Please specify a valid option: create a file, create a folder, delete a file, delete a folder, or exit.")
    return True

def process_create_file():
    drive_response = listen("In which drive do you want to create a new file?")
    drive_letter = parse_drive(drive_response)
    if drive_letter and drive_letter in "CDE":
        file_name = listen("What is the name of the file? Please include the file extension.")
        path = f"{drive_letter}:/"
        file_path = os.path.join(path, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write('')
            speak(f"File '{file_name}' created successfully.")
        else:
            speak("File already exists.")
    else:
        speak("Please specify a valid drive like 'C drive' or 'D drive'.")

def process_delete_file():
    file_path = listen("Please specify the full path of the file you want to delete.")
    delete_folder_or_file(file_path)

def main():
    continue_program = True
    while continue_program:
        continue_program = process_user_choice()

if __name__ == "__main__":
    main()
