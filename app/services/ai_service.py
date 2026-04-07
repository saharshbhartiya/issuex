import json
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

def analyze_issue(title: str , body: str):
    print("Calling AI")
    prompt = f"""
    Analyze this GitHub issue :

    Title :{title}
    Description: {body}

    Rules:
    - Output ONLY valid JSON
    - No explanation outside JSON
    - No extra text

    Format:
    {{
        "skill": "Frontend/Backend/Fullstack/DevOps/Unknown",
        "difficulty": "Easy/Medium/Hard",
        "explanation": "short explanation in 2-3 lines"
    }}

    Do not add any extra text.
    """
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [
            {"role" : "user" , "content" : prompt}
        ],
        temperature=0
    )

    text = response.choices[0].message.content.strip()

    try:
        return json.loads(text)
    except:
        return {
            "skill": "Unknown",
            "difficulty": "Medium",
            "explanation": text
        }