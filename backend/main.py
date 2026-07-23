from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from parser import extract_text
from ats import analyze_ats
from ai_analyzer import analyze_resume

import os
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "https://ats-resume-analyzer-seven.vercel.app",
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "ATS Resume Analyzer Backend Running"}


@app.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join("uploads", resume.filename)

        with open(file_path, "wb") as f:
            f.write(await resume.read())

        # -----------------------------
        # Extract Resume Text
        # -----------------------------
        start = time.time()

        resume_text = extract_text(file_path)

        print("PDF Extraction:", round(time.time() - start, 2), "seconds")

        # -----------------------------
        # ATS Analysis
        # -----------------------------
        start = time.time()

        ats_result = analyze_ats(
            resume_text,
            job_description
        )

        print("Python ATS:", round(time.time() - start, 2), "seconds")

        # -----------------------------
        # AI Suggestions
        # -----------------------------
        start = time.time()

        ai_result = analyze_resume(
            ats_result["score"],
            ats_result["matching_skills"],
            ats_result["missing_skills"]
        )

        print("Gemini API:", round(time.time() - start, 2), "seconds")

        suggestions = ai_result.get("suggestions", [])
        ai_generated = ai_result.get("ai_generated", False)

        if ai_generated:
            message = ""
        else:
            message = "AI suggestions are currently unavailable."

        if os.path.exists(file_path):
            os.remove(file_path)

        return {
            "score": ats_result["score"],
            "matching_skills": ats_result["matching_skills"],
            "missing_skills": ats_result["missing_skills"],
            "suggestions": suggestions,
            "ai_generated": ai_generated,
            "message": message,
        }

    except Exception as e:
        print("Backend Error:", str(e))

        return {
            "score": 0,
            "matching_skills": [],
            "missing_skills": [],
            "suggestions": [],
            "ai_generated": False,
            "message": "Unable to analyze the resume.",
        }