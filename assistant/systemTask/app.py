import subprocess

def find_application_path(app_name):
    """Function to find an application path using the 'where' command."""
    try:
        # Normalize the application name to include '.exe' if not already present
        if not app_name.lower().endswith(".exe"):
            app_name += ".exe"
        
        # Using 'where' command to find the application
        result = subprocess.run(["where", app_name], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.splitlines()[0]  # Return the first match
        else:
            return None
    except Exception as e:
        print(f"Error finding application: {str(e)}")
        return None

def open_application(app_name):
    """Function to open an application."""
    app_path = find_application_path(app_name)
    if app_path:
        subprocess.Popen([app_path], shell=True)
        speak(f"Opening {app_name}")
    else:
        speak("Application not found. Please try again.")

