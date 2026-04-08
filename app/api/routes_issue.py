from fastapi import APIRouter , Query
from typing import List, Optional
from app.services.github_service import fetch_issues
from app.schemas.issue_schema import IssueResponse
from app.services.recommendation_service import recommend_issues
from fastapi import BackgroundTasks

router = APIRouter()

@router.get("/issues" , response_model=List[IssueResponse])

def get_issues(
    background_tasks: BackgroundTasks,
    repo: str = Query(... , description= "Repository must be in owner/repo format."),
    page: int = Query(1 , ge=1 , description= "Page number must be >= 1"),
    skill: Optional[str] = Query(None),
    level : Optional[str] = "Beginner"
):
    issues = fetch_issues(repo , page , background_tasks)

    return  recommend_issues(issues , skill , level)