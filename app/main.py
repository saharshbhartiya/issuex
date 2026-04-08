from fastapi import FastAPI
from app.api.routes_issue import router as issue_router

app = FastAPI()


@app.get("/")
def home():
    return {"message" : "IssueX running"}

app.include_router(issue_router)