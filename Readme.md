# 📫IssueX

**Navigate open source with AI**

IssueX is a system that helps developers to find and understand GitHub issues efficiently. It fetches issues from any repository, filters relevant data, and prepares the foundation for intelligent recommendations.

---

## 📌 Current Features

* Fetch issues from any GitHub repository
* Pagination support
* Pull request filtering
* Clean and structured API response

---

## ⚙️ Tech Stack

* Backend: Python + FastAPI
* API: GitHub REST API

---

## 🔗 API Endpoint

### Get Issues

```
GET /issues?repo=owner/repo&page=1
```

### Example

```
/issues?repo=facebook/react&page=1
```

### Response

```json
[
  {
    "title": "Issue title",
    "url": "https://github.com/...",
    "number": 123,
    "labels": ["bug"]
  }
]
```

---

## 🚀 How to Run

1. Clone the repository
2. Create virtual environment
3. Install dependencies

```
pip install -r requirements.txt
```

4. Run server

```
uvicorn app.main:app --reload
```

---

## 📁 Project Structure

```
app/
 ├── main.py
 ├── api/
 ├── services/
```

---

## 🧠 Upcoming Features

* AI-based issue understanding
* Skill-based recommendations
* Database integration

---

## 📜 License

MIT License
