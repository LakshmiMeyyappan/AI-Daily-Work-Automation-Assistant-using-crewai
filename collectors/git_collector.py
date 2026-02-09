import requests
from datetime import datetime, timezone

def get_git_activity(github_username: str):
    url = f"https://api.github.com/users/{github_username}/events/public"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return ["Unable to fetch GitHub activity"]

    events = response.json()
    today = datetime.now(timezone.utc).date()

    push_repos_today = set()

    for event in events:
        # Only care about Push events
        if event.get("type") == "PushEvent":
            created_at = event.get("created_at")
            if not created_at:
                continue

            event_date = datetime.fromisoformat(
                created_at.replace("Z", "+00:00")
            ).date()

            # Only today’s pushes
            if event_date == today:
                repo_name = event.get("repo", {}).get("name")
                if repo_name:
                    push_repos_today.add(repo_name)

    if not push_repos_today:
        return ["No GitHub push activity today"]

    # Human-readable summary
    return [
        f"Pushed updates to {repo}"
        for repo in sorted(push_repos_today)
    ]
