# collectors/vscode_collector.py
import os, json

def get_vscode_activity():
    vscode_dir = os.path.expanduser("~/.config/Code/User")

    settings = os.path.join(vscode_dir, "settings.json")

    if not os.path.exists(settings):
        return {"editor": "VS Code", "status": "Used"}

    return {
        "editor": "VS Code",
        "status": "Active"
    }
