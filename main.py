import os
import urllib.request

CURRENT_VERSION = "1.0.1"
VERSION_URL = "https://raw.githubusercontent.com/TheChii/Self-Updater-Template/main/version.txt"  
UPDATE_URL = "https://raw.githubusercontent.com/TheChii/Self-Updater-Template/main/main.py"    

def check_for_updates():
    try:
        response = urllib.request.urlopen(VERSION_URL)
        latest_version = response.read().decode('utf-8').strip()

        if latest_version > CURRENT_VERSION:
            print(f"Update available: {latest_version}")
            return latest_version
        else:
            print("You are using the latest version.")
            return None
    except Exception as e:
        print(f"Failed to check for updates: {e}")
        return None

def download_update():
    try:
        response = urllib.request.urlopen(UPDATE_URL)
        new_program = response.read().decode('utf-8')
        return new_program
    except Exception as e:
        print(f"Failed to download update: {e}")
        return None

def apply_update(new_code):
    try:
        current_file = os.path.abspath(__file__)
        with open(current_file, 'w') as file:
            file.write(new_code)
        print("Update applied successfully.")
    except Exception as e:
        print(f"Failed to apply update: {e}")

def main_program():
    print("Running the main program...")

if __name__ == "__main__":
    latest_version = check_for_updates()
    if latest_version:
        new_code = download_update()
        if new_code:
            apply_update(new_code)
    else:
        main_program()
