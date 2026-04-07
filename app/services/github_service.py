import requests
from fastapi import HTTPException
from app.services.ai_service import analyze_issue
from typing import Optional

cache = {}

def fetch_issues(repo: str , page : int , skill : Optional[str]):
    try:
        owner , repo_name = repo.split("/")
    except ValueError:
        raise HTTPException(
            status_code= 400,
            detail= "Invalid repo format. Use owner/repo"
        )
    
    key = f"{owner}_{repo_name}_{page}_{skill}"

    if key in cache:
        return cache[key]
    
    url = f"https://api.github.com/repos/{owner}/{repo_name}/issues"

    params = {
        "page" : page,
        "per_page" : 10,
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
    max_call = 3
    count = 0

    for item in data:

        if "pull_request" in item:
            continue

        labels =  [label["name"] for label in item.get("labels" , [])]
        labels_text = ", ".join(labels)
        body = item.get("body") or ""

        if count < max_call :
            ai_result = analyze_issue(
                item.get("title" , "") , 
                body + f" Labels: {labels_text}"
            )
            count += 1
        else:
            ai_result = {
                "skill" : "Unknown",
                "difficulty" : "Unknown",
                "explanation" : "AI analysis skipped"
            }
        issues.append({
            "title" : item.get("title"),
            "url" : item.get("html_url"),
            "number" : item.get("number"),
            "labels" : labels,
            "analysis" : ai_result
        })
    cache[key] = issues
    return issues