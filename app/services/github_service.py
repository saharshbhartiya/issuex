import requests

def fetch_issues(repo: str , page : int):
    try:
        owner , repo_name = repo.split("/")
    except ValueError:
        return {"message" : "Invalid repo format. Use owner/repo"}
    
    url = f"https://api.github.com/repos/{owner}/{repo_name}/issues"

    params = {
        "page" : page,
        "per_page" : 5,
        "state" : "open"
    }

    response = requests.get(url , params=params)

    if response.status_code == 404:
        return {"error" : "Repository not Found"}
    
    if response.status_code != 200:
        return {"error" : "GitHub API error"}
    
    data = response.json()

    issues = []

    for item in data:
        if "pull_requests" in item:
            continue

        issues.append({
            "title" : item.get("title"),
            "url" : item.get("html_url"),
            "number" : item.get("number"),
            "label" : [label["name"] for label in item.get("labels" , [])]
        })

    return issues