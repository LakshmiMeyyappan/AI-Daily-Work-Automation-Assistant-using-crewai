import os
import time
import threading
from voice_generator import morning_briefing
from report_generator import show_report

def run_morning():
    print("--- Starting Your Morning Assistant ---")
    
    # 1. Brief pause to let the system initialize
    time.sleep(3) 

    reports_dir = "reports"
    
    # 2. Locate the most recent report file
    if not os.path.exists(reports_dir) or not os.listdir(reports_dir):
        print("Error: No reports found. Did you run the nightly process?")
        return

    files = [os.path.join(reports_dir, f) for f in os.listdir(reports_dir) if f.endswith(".txt")]
    latest_report_path = max(files, key=os.path.getctime)

    with open(latest_report_path, "r", encoding="utf-8") as f:
        full_content = f.read()

    # 3. EXTRACTION LOGIC (The "Filter")
    # This removes the logs and only grabs the task list
    marker = "TODAY'S TASKS"
    if marker in full_content.upper():
        start_pos = full_content.upper().find(marker)
        # Get everything after the marker and remove conversational 'fluff'
        raw_tasks = full_content[start_pos + len(marker):].split("I hope this helps")[0].strip()
        display_text = raw_tasks.lstrip(':-* \n\r')
    else:
        # Fallback if the specific header isn't found
        display_text = "No specific task list found. Please check your full report."

    # 4. RUN VOICE AND UI TOGETHER (Parallel)
    print("Opening your tasks and starting the briefing...")
    
    # We send ONLY the clean display_text to the voice so it doesn't read logs
    threading.Thread(target=morning_briefing, args=(display_text,)).start()
    
    # Show the popup window with the correct title
    show_report(display_text, title="Today's Mission")

if __name__ == "__main__":
    run_morning()