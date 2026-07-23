import re

SKILLS = [
    "python",
    "java",
    "fastapi",
    "flask",
    "django",
    "mysql",
    "postgresql",
    "mongodb",
    "sql",
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
    "linux",
    "rest api",
    "redis",
    "javascript",
    "react",
    "html",
    "css"
]


def analyze_ats(resume_text, job_description):

    resume = resume_text.lower()
    jd = job_description.lower()

    matching = []
    missing = []

    for skill in SKILLS:
        if skill in jd:
            if skill in resume:
                matching.append(skill.title())
            else:
                missing.append(skill.title())

    if len(matching) + len(missing) == 0:
        score = 0
    else:
        score = round(
            len(matching)
            / (len(matching) + len(missing))
            * 100
        )

    return {
        "score": score,
        "matching_skills": matching,
        "missing_skills": missing
    }