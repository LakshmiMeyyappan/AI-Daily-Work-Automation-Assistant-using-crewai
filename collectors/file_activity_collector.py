# collectors/file_activity_collector.py

from pathlib import Path
import datetime

def get_file_activity(base_dir="."):
    today = datetime.date.today()
    touched_files = []

    for file in Path(base_dir).rglob("*"):
        if file.is_file() and file.suffix in [".py", ".ipynb", ".md"]:
            modified_date = datetime.date.fromtimestamp(file.stat().st_mtime)
            if modified_date == today:
                touched_files.append(str(file))

    return {
        "files_worked_today": touched_files[:20],  # limit
        "total_files": len(touched_files)
    }
