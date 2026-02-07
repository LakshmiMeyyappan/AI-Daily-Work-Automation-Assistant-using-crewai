# collectors/terminal_collector.py
import os

def get_terminal_activity():
    history = os.path.expanduser("~/.bash_history")
    if not os.path.exists(history):
        return {"tools_used": []}

    with open(history, "r", errors="ignore") as f:
        commands = f.readlines()[-50:]

    keywords = ["git", "python", "pip", "docker", "sql"]
    tools = list(set(
        k for cmd in commands for k in keywords if k in cmd
    ))

    return {"tools_used": tools}
