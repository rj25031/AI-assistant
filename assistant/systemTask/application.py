import subprocess
import webbrowser

def find_application_path(app_name):
    try:
        # Normalize application name
        app_name = app_name.lower()
        
        # Check if the application name ends with ".exe", if not, append it
        if not app_name.endswith(".exe"):
            if app_name == "code":
                app_name = "code"
            else:
                app_name += ".exe"
        
        # Run the "where" command to search for the application
        result = subprocess.run(["where", app_name], capture_output=True, text=True)
        
        if result.returncode == 0:
            # If the command is successful, return the path of the first result
            return result.stdout.strip()
        else:
            # If the command fails or the application is not found, return None
            return None
    except Exception as e:
        print(f"Error finding application: {str(e)}")
        return None

def open_application(app_name):
    # Normalize application name
    app_name = app_name.lower()

    # Special case for opening calculator
    if app_name == "calculator":
        try:
            subprocess.Popen("calc.exe")
            return f"Opening {app_name}"
        except Exception as e:
            print(f"Error opening {app_name}: {str(e)}")
            return f"Error opening {app_name}"


    # For other applications, find the path using find_application_path function
    app_path = find_application_path(app_name)
    
    if app_path:
        try:
            # Open the application using subprocess
            subprocess.Popen([app_path], shell=True)
            return f"Opening {app_name}"
        except Exception as e:
            print(f"Error opening {app_name}: {str(e)}")
            return f"Error opening {app_name}"
    else:
        try:
            # If the application is not found, attempt to open a web browser
            app = app_name.replace(" ","")
            url = f"https://www.{app}.com"
            webbrowser.open(url)
            return f"Opening {app_name}"
        except Exception as e:
            print(f"Error opening web browser: {str(e)}")
            return f"Error opening {app_name}"

