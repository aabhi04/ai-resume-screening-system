from .skill_extractor import extract_skills
from .matching import calculate_match_score


def run_pipeline(resume_text, job_description_text):
    # Extract skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description_text)

    # Calculate score
    score, matched_skills = calculate_match_score(resume_skills, job_skills)

    # Return structured result
    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "match_score": score
    }
