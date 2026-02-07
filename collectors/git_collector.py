import requests

def get_github_username():
    try:
        with open("github_user.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def get_git_activity():
    username = get_github_username()

    if not username:
        return ["GitHub username not configured"]

    url = f"https://api.github.com/users/{username}/events/public"

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "AI-Daily-Work-Assistant"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return ["Unable to fetch GitHub activity"]

    events = response.json()
    commits_today = []

    for event in events:
        if event.get("type") == "PushEvent":
            payload = event.get("payload", {})
            commits = payload.get("commits", [])

            for commit in commits:
                message = commit.get("message", "No message")
                commits_today.append(message)

    if not commits_today:
        return ["No GitHub commits today"]

    return commits_today
