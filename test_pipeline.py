from src.pipeline import run_pipeline

resume = """
I am a B.Tech graduate with experience in Python, Machine Learning,
SQL, TensorFlow and strong problem solving skills.
"""

job_description = """
We are hiring a developer skilled in Python, SQL,
Deep Learning and communication skills.
"""

result = run_pipeline(resume, job_description)

print("\n===== AI Resume Screening Report =====\n")

print("Extracted Resume Skills:")
print(", ".join(result["resume_skills"]))

print("\nExtracted Job Skills:")
print(", ".join(result["job_skills"]))

print("\nMatched Skills:")
print(", ".join(result["matched_skills"]))

print(f"\nFinal Match Score: {result['match_score']}%")
