from crewai import Task


def create_tasks(activity_data):
    analyze = Task(
        description=(
            f"Analyze this technical data: {activity_data}. "
            "CRITICAL: Do not repeat, quote, or display any JSON blocks or raw logs. "
            "Provide ONLY a human-readable summary of accomplishments."
        ),
        expected_output="Plain text bullet points of wins. No code blocks. No JSON.",
        name="work_analysis"
    )
    
    plan = Task(
        description=(
            "Based on the previous analysis, create 5 tasks for the next session. "
            "Use the heading 'TODAY'S TASKS'. Write filenames naturally without .py. "
            "Do not include any raw data logs."
        ),
        expected_output="A list of 5 tasks starting with 'TODAY'S TASKS'.",
        name="next_steps"
    )
    return [analyze, plan]