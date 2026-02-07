import requests

GITHUB_USERNAME = "YOUR_GITHUB_USERNAME"

def get_git_activity():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/events/public"
    response = requests.get(url)

    if response.status_code != 200:
        return ["Unable to fetch GitHub activity"]

    events = response.json()
    commits_today = []

    for event in events:
        # ✅ ONLY handle push events
        if event.get("type") == "PushEvent":
            payload = event.get("payload", {})
            commits = payload.get("commits", [])

            for commit in commits:
                message = commit.get("message", "No message")
                commits_today.append(message)

    if not commits_today:
        return ["No GitHub commits today"]

    return commits_today
