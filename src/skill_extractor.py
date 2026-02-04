# src/skill_extractor.py

SKILL_DB = [
    "python", "java", "c", "c++", "sql",
    "machine learning", "deep learning", "nlp",
    "data science", "data analysis",
    "tensorflow", "pytorch", "scikit-learn",
    "pandas", "numpy",
    "flask", "django",
    "git", "docker", "aws"
]


def extract_skills(text: str):
    """
    Extracts skills from resume text using keyword matching.
    """

    text = text.lower()
    found_skills = []

    for skill in SKILL_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))  # remove duplicates
