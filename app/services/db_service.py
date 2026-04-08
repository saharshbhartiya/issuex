from app.db.database import SessionLocal
from app.models.issue_model import Issue

def save_issue(repo , issue_data):
    db = SessionLocal()

    issue = Issue(
        repo = repo,
        title = issue_data["title"],
        url = issue_data["url"],
        number = issue_data["number"],
        labels = ",".join(issue_data["labels"]), 
        skill = issue_data["analysis"]["skill"],
        difficulty = issue_data["analysis"]["difficulty"],
        explanation = issue_data["analysis"]["explanation"]
    )

    db.add(issue)
    db.commit()
    db.close()

def get_issues_from_db(repo):
    db = SessionLocal()

    issues = db.query(Issue).filter(Issue.repo == repo).all()
    db.close()
    return issues

def convert_db_todict(db_issues):
    result = []

    for i in db_issues:
        result.append({
            "title":i.title,
            "url": i.url,
            "number": i.number,
            "labels": i.labels.split(","),
            "analysis": {
                "skill": i.skill,
                "difficulty": i.difficulty,
                "explanation": i.explanation
            }
        })
    return result