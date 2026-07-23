import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)


def analyze_resume(score, matching_skills, missing_skills):

    prompt = f"""
You are an ATS Resume Advisor.

ATS Score:
{score}

Matching Skills:
{", ".join(matching_skills)}

Missing Skills:
{", ".join(missing_skills)}

Give exactly 3 short resume improvement suggestions.

Return ONLY valid JSON.

{{
    "suggestions": [
        "Suggestion 1",
        "Suggestion 2",
        "Suggestion 3"
    ]
}}

Do not use markdown.
Return JSON only.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        text = response.text.strip()
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        data = json.loads(text)

        return {
            "suggestions": data["suggestions"],
            "ai_generated": True,
        }

    except Exception as e:
        print(f"Gemini Error: {e}")

        return {
            "suggestions": [],
            "ai_generated": False,
        }