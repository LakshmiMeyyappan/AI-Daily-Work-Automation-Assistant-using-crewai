# Project: AI Daily Work Assistant v1.1

import os
import sys
from datetime import datetime

from crew_runner import run_nightly_process
from morning_runner import run_morning
import os
os.environ["LITELLM_LOG"] = "ERROR"
os.environ["LITELLM_DISABLE_LOGGING"] = "true"



def setup_config():
    """Handles both API Key and GitHub Username setup"""
    api_file = "api_key.txt"
    user_file = "github_user.txt"
    needs_restart = False

    # Check API Key
    if not os.path.exists(api_file):
        with open(api_file, "w") as f:
            f.write("PASTE_YOUR_GROQ_KEY_HERE")
        print("[!] Created 'api_key.txt'. Please paste your Groq API Key.")
        needs_restart = True
    
    # Check GitHub Username
    if not os.path.exists(user_file):
        with open(user_file, "w") as f:
            f.write("ENTER_GITHUB_USERNAME_HERE")
        print("[!] Created 'github_user.txt'. Please enter your GitHub username.")
        needs_restart = True

    if needs_restart:
        print("\n--- SETUP REQUIRED ---")
        print("Please fill in the text files created in the folder and restart.")
        os.system("pause")
        sys.exit()

    # Load and return the key
    return open(api_file, "r").read().strip()

def main():
    current_hour = datetime.now().hour
    print(f"--- AI Assistant (Current Time: {datetime.now().strftime('%H:%M')}) ---")

    if current_hour >= 16:
        print("Detected: End of day. Analyzing your work...")
        run_nightly_process()
    else:
        print("Detected: Start of day. Preparing your briefing...")
        run_morning()

    print("\nProcess finished.")
    os.system("pause")

if __name__ == "__main__":
    try:
        # Combined setup
        os.environ["GROQ_API_KEY"] = setup_config()
        main()
    except Exception as e:
        print("\n--- CRITICAL ERROR ---")
        print(f"Details: {e}")
        input("\nPress ENTER to close...")