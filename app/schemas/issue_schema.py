from pydantic import BaseModel
from typing import List

class Analysis(BaseModel):
    skill: str
    difficulty: str
    explanation: str

class IssueResponse(BaseModel):
    title: str
    url: str
    number: int
    labels: List[str]
    analysis: Analysis