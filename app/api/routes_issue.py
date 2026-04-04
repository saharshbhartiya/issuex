from fastapi import APIRouter
from app.services.github_service import fetch_issues

router = APIRouter()

@router.get("/issues")
def get_issues(repo:str , page: int = 1):
    result = fetch_issues(repo , page)
    return result