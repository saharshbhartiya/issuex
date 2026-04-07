def recommend_issues(issues , user_skill: str):
    if not user_skill:
        return issues
    
    matched = []

    for issue in issues:
        issue_skill = issue["analysis"]["skill"]

        if issue_skill and issue_skill.lower() == user_skill.lower():
            matched.append(issue)
    return matched