import requests
from fastapi import HTTPException


cache = {}


def fetch_issues(repo: str , page : int):
    try:
        owner , repo_name = repo.split("/")
    except ValueError:
        raise HTTPException(
            status_code= 400,
            detail= "Invalid repo format. Use owner/repo"
        )
    
    key = f"{repo_name}_{page}"

    if key in cache:
        print("Fetching from Cache")
        return cache[key]
    
    url = f"https://api.github.com/repos/{owner}/{repo_name}/issues"

    params = {
        "page" : page,
        "per_page" : 5,
        "state" : "open"
    }

    response = requests.get(url , params=params)

    if response.status_code == 404:
        raise HTTPException(
            status_code= 404,
            detail= "Repository not found with : " + owner +"/"+repo_name
        )
    
    if response.status_code != 200:
        raise HTTPException(
            status_code= 500,
            detail= "Github API error"
        )
    
    data = response.json()

    issues = []

    for item in data:
        if "pull_request" in item:
            continue

        issues.append({
            "title" : item.get("title"),
            "url" : item.get("html_url"),
            "number" : item.get("number"),
            "labels" : [label["name"] for label in item.get("labels" , [])]
        })
    cache[key] = issues
    print("Fetching from Github")
    return issues