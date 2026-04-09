from sqlalchemy import Column, Integer, String, Text
from app.db.database import Base

class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True , index=True)
    repo = Column(String)
    title = Column(String)
    url = Column(String)
    number = Column(Integer)
    labels = Column(String)
    skill = Column(String)
    difficulty = Column(String)
    explanation = Column(Text)
    page = Column(Integer)