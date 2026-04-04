from fastapi import APIRouter , Query
from typing import List
from app.services.github_service import fetch_issues
from app.schemas.issue_schema import IssueResponse

router = APIRouter()

@router.get("/issues" , response_model=List[IssueResponse])
def get_issues(
    repo: str = Query(... , description= "Repository must be in owner/repo format."),
    page: int = Query(1 , ge=1 , description= "Page number must be >= 1")
):
    return fetch_issues(repo , page)