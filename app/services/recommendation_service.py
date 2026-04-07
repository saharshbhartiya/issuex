def recommend_issues(issues, user_skill: str, user_level: str = "Beginner"):
    scored_issues = []

    for issue in issues:
        score = calculate_score(issue, user_skill, user_level)
        scored_issues.append((score, issue))

    scored_issues.sort(key=lambda x: x[0], reverse=True)

    return [issue for score, issue in scored_issues]


def calculate_score(issue, user_skill: str, user_level: str = "Beginner"):
    score = 0

    analysis = issue.get("analysis", {})
    issue_skill = analysis.get("skill", "")
    issue_difficulty = analysis.get("difficulty", "")

    if user_skill and issue_skill and user_skill.lower() in issue_skill.lower():
        score += 5

    if user_level == "Beginner" and issue_difficulty == "Easy":
        score += 3
    elif user_level == "Intermediate" and issue_difficulty == "Medium":
        score += 3
    elif user_level == "Advanced" and issue_difficulty == "Hard":
        score += 3

    labels = issue.get("labels", [])
    if any("good first issue" in l.lower() for l in labels):
        score += 2

    return score