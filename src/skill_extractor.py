# src/skill_extractor.py

from .preprocessing import clean_text, remove_stopwords
import re

# ROLE BASED SKILL DATABASE

ROLE_SKILLS = {

    "ai_ml_engineer": [
        "python", "machine learning", "deep learning", "nlp",
        "tensorflow", "pytorch", "scikit-learn",
        "sql", "pandas", "numpy",
        "communication", "problem solving"
    ],

    "soc_analyst": [
        "cybersecurity", "siem", "splunk", "qradar",
        "incident response", "threat detection",
        "malware", "phishing", "ransomware",
        "tcp/ip", "dns", "firewall",
        "ids", "ips", "vulnerability assessment",
        "risk analysis", "linux", "windows",
        "python", "powershell",
        "communication", "problem solving"
    ],

    "data_analyst": [
        "python", "sql", "excel", "power bi",
        "tableau", "pandas", "numpy",
        "data visualization", "statistics",
        "communication"
    ]
}


from .preprocessing import clean_text, remove_stopwords


def extract_skills(text, role):
    text = clean_text(text)
    text = remove_stopwords(text)

    skills_list = ROLE_SKILLS.get(role, [])

    found_skills = []

    for skill in skills_list:
        if re.search(rf"\b{re.escape(skill)}\b", text):
            found_skills.append(skill)

    return list(set(found_skills))
