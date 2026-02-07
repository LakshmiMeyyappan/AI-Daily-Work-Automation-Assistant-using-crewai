import os
from collectors.file_activity_collector import get_file_activity
from collectors.git_collector import get_git_activity
from collectors.terminal_collector import get_terminal_activity
from collectors.vscode_collector import get_vscode_activity

from agents import work_agent, planner_agent
from tasks import create_tasks
from crewai import Crew
from report_generator import generate_report, show_report

#os.environ["LITELLM_LOG"] = "ERROR"
#os.environ["LITELLM_DISABLE_LOGGING"] = "true"


if "GROQ_API_KEY" not in os.environ:
    if os.path.exists("api_key.txt"):
        with open("api_key.txt") as f:
            os.environ["GROQ_API_KEY"] = f.read().strip()

def run_nightly_process():
    print("--- Starting End-of-Day AI Analysis ---")

    # 1. Collect all activity from your laptop
    activity = {
        "files": get_file_activity(),
        "git": get_git_activity(),
        "terminal": get_terminal_activity(),
        "vscode": get_vscode_activity()
    }

    # 2. Initialize Tasks and assign Agents
    all_tasks = create_tasks(activity)
    
    # Task 0 is Work Analysis, Task 1 is Planning
    all_tasks[0].agent = work_agent
    all_tasks[1].agent = planner_agent

    # 3. Run the Crew
    crew = Crew(
        agents=[work_agent, planner_agent],
        tasks=all_tasks,
        verbose=True
    )

    print("\n[AI is thinking about your day...]")
    crew.kickoff()

    # 4. MANUALLY COMBINE OUTPUTS
    # This prevents the "Empty Window" or "Missing Task" issues.
    # We use Task[0] for accomplishments and Task[1] for the plan.
    
    todays_wins = all_tasks[0].output.raw
    future_plan = all_tasks[1].output.raw

    # Create the full text for the file (used by morning_runner)
    # We inject the "NEXT STEPS" marker strictly here to ensure splitting works.
    full_report_content = (
        "TODAY'S ACCOMPLISHMENTS\n"
        "-----------------------\n"
        f"{todays_wins}\n\n"
        "NEXT STEPS\n"
        "-----------------------\n"
        f"{future_plan}"
    )

    # 5. Save the FULL report to a file
    report_path = generate_report(full_report_content)
    print(f"\n[Success] Full report saved to: {report_path}")

    # 6. SHOW THE NIGHTLY POPUP (Only Accomplishments)
    # We show the user only their wins so they can rest well.
    night_display_text = (
        "GREAT WORK TODAY!\n\n"
        "HERE IS WHAT YOU ACCOMPLISHED:\n"
        f"{todays_wins}"
    )
    
    print("Opening your nightly achievement summary...")
    show_report(night_display_text)

    print("\nDaily AI Work Assistant Completed Successfully. Good night!")

if __name__ == "__main__":
    run_nightly_process()