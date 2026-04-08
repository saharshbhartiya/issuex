# 🚀 IssueX

**Navigate open source with intelligence**

IssueX is an AI-powered backend system that helps developers discover, understand, and prioritize GitHub issues based on their skills and experience level.

---

## 🧠 Problem

Finding the right issue in open source is difficult:

* Issues are often vague or poorly described
* No clear difficulty level
* Hard to match with your skill set
* Beginners don’t know where to start

---

## 💡 Solution

IssueX solves this by:

* 🔍 Fetching issues from any GitHub repository
* 🧠 Analyzing issues using AI (Groq)
* 🎯 Matching issues with user skill and level
* 📊 Ranking issues based on relevance

---

## ⚙️ Features

* GitHub issue fetching with pagination
* Pull request filtering
* AI-powered issue analysis (skill, difficulty, explanation)
* Skill-based recommendation system
* Ranking system using scoring logic
* In-memory caching for performance

---

## 🧱 System Architecture

```
User Request
     ↓
FastAPI Route (Controller)
     ↓
GitHub Service (Fetch + Cache)
     ↓
AI Service (Groq Analysis)
     ↓
Recommendation Engine (Scoring + Ranking)
     ↓
Response (Structured JSON)
```

---

## 📊 Recommendation Logic

Issues are ranked based on:

* Skill match
* Difficulty match (Beginner / Intermediate / Advanced)
* Labels like `good first issue`

---

## 🔗 API Endpoints

### Get Issues

```
GET /issues
```

### Query Parameters

| Parameter | Description                                   |
| --------- | --------------------------------------------- |
| repo      | Repository in `owner/repo` format             |
| page      | Page number (default = 1)                     |
| skill     | Skill filter (Frontend, Backend, etc.)        |
| level     | User level (Beginner, Intermediate, Advanced) |

---

### Example Request

```
/issues?repo=facebook/react&page=1&skill=Frontend&level=Beginner
```

---

### Example Response

```json
[
  {
    "title": "Bug:",
    "url": "https://github.com/...",
    "number": 123,
    "labels": ["Status: Unconfirmed"],
    "analysis": {
      "skill": "Frontend",
      "difficulty": "Easy",
      "explanation": "This issue relates to React UI behavior..."
    }
  }
]
```

---

## 📁 Project Structure

```
app/
 ├── api/
      ├── routes_issue.py
 ├── services/
 │    ├── github_service.py
 │    ├── ai_service.py
 │    ├── recommendation_service.py
 ├── schemas/
      ├── issue_schema.py
 ├── main.py
```

---

## 🚀 Getting Started

### 1. Clone repository

```
git clone <your-repo-url>
cd issuex
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Run server

```
uvicorn app.main:app --reload
```

---

## ⚠️ Notes

* API key is required to use this

---

## 🔮 Future Improvements

* Database integration (PostgreSQL)
* Vector search for semantic matching
* Chrome extension integration
* Personalized learning path
* Async processing for faster responses

---

## 🤝 Contributing

Contributions are welcome. Feel free to open issues or submit pull requests.

---

## 📜 License

[MIT LICENSE]
