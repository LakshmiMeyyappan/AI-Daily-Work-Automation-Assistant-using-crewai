import os
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext

def generate_report(content):
    """Saves the AI output to a dated text file."""
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    # File naming: daily_report_2026-02-02.txt
    file_name = f"daily_report_{datetime.now().strftime('%Y-%m-%d')}.txt"
    report_path = os.path.join(reports_dir, file_name)

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(content)

    return report_path


def open_report(path):
    """Opens the text file in the default system editor (Notepad, etc.)"""
    try:
        os.startfile(path)
    except Exception as e:
        print(f"Could not open file automatically: {e}")


def show_report(text, title="Daily AI Assistant"):
    """Creates a clean popup window to display the report."""
    root = tk.Tk()
    root.title(title)
    root.geometry("750x550")
    
    # Make it appear on top of other windows
    root.attributes('-topmost', True)

    # Determine Header Text based on the title/content
    header_text = "Today's Achievements" if "Mission" not in title else "Today's Work Plan"
    button_text = "Close" if "Mission" not in title else "Start My Day"
    button_color = "#2196F3" if "Mission" not in title else "#4CAF50" # Blue for night, Green for morning

    label = tk.Label(root, text=header_text, font=("Segoe UI", 16, "bold"), pady=15)
    label.pack()

    # Using ScrolledText in case the list of tasks is long
    text_box = scrolledtext.ScrolledText(
        root, wrap="word", font=("Consolas", 11), bg="#ffffff", 
        padx=20, pady=20, spacing1=8)
    
    text_box.insert("1.0", text)
    text_box.config(state="disabled") # Prevent editing
    text_box.pack(expand=True, fill="both", padx=10)

    # Close button with dynamic text/color
    close_button = tk.Button(
        root, text=button_text, command=root.destroy, bg=button_color, fg="white", 
        font=("Segoe UI", 11, "bold"),width=20,pady=5
    )
    close_button.pack(pady=15)

    root.mainloop()