from src.skill_extractor import extract_skills
from src.matching import calculate_match_score

resume = """
I have experience in Python, Machine Learning, SQL and TensorFlow.
Strong problem solving and teamwork skills.
"""

job_description = """
Looking for a candidate skilled in Python, SQL, Deep Learning and communication.
"""

resume_skills = extract_skills(resume)
job_skills = extract_skills(job_description)

score, matched = calculate_match_score(resume_skills, job_skills)

print("Resume Skills:", resume_skills)
print("Job Skills:", job_skills)
print("Matched Skills:", matched)
print("Match Score:", score, "%")
