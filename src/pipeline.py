from .skill_extractor import extract_skills
from .matching import calculate_match_score


def run_pipeline(resume_text, job_description_text, role):

    resume_skills = extract_skills(resume_text, role)
    job_skills = extract_skills(job_description_text, role)

    score, matched_skills = calculate_match_score(resume_skills, job_skills)

    missing_skills = list(set(job_skills) - set(resume_skills))

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": score
    }
