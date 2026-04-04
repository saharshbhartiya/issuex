from pydantic import BaseModel
from typing import List

class IssueResponse(BaseModel):
    title: str
    url: str
    number: int
    labels: List[str]