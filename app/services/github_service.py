import requests
from fastapi import HTTPException
from app.services.ai_service import analyze_issue
from app.services.db_service import get_issues_from_db, save_issue , convert_db_todict

cache = {}

def fetch_issues(repo: str , page : int , background_tasks : None):
    db_issues = get_issues_from_db(repo , page)

    if db_issues:
        valid = [i for i in db_issues if i.skill != "Processing"]

        if valid:
            print("Fetching from DB")
            return convert_db_todict(valid)
    
    try:
        owner , repo_name = repo.split("/")
    except ValueError:
        raise HTTPException(
            status_code= 400,
            detail= "Invalid repo format. Use owner/repo"
        )
    
    key = f"{owner}_{repo_name}_{page}"

    if key in cache:
        cached = cache[key]

        if any(i["analysis"]["skill"] == "Processing" for i in cached):
            print("Cache has processing data , skipping cache")
        else:
            print("Fetching from cache")
            return cached
    
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

        if count < max_call :
         
            background_tasks.add_task(process_issue_async , repo , item , page)

            count += 1


        issues.append({
            "title" : item.get("title"),
            "url" : item.get("html_url"),
            "number" : item.get("number"),
            "labels" : labels,
            "analysis" : {
                "skill" : "Processing",
                "difficulty" : "Processing",
                "explanation" : "Analysis in progress..."
            }
        })
    cache[key] = issues
    return issues

def process_issue_async(repo , item , page):
    labels = [label["name"] for label in item.get("labels" ,[])]
    body = item.get("body") or ""

    ai_result = analyze_issue(
        item.get("title" , ""),
        body + f" Labels: {','.join(labels)}"
    )

    issue_data = {
        "title" : item.get("title"),
        "url" : item.get("html_url"),
        "number" : item.get("number"),
        "labels" : labels,
        "analysis" : ai_result
    }
    
    save_issue(repo , issue_data , page)
    