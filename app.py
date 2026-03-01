import streamlit as st
from src.pipeline import run_pipeline



st.set_page_config(page_title="AI Resume Screening System", layout="centered")

st.title(" AI Resume Screening System")
role = st.selectbox(
    "Select Job Role",
    ["ai_ml_engineer", "soc_analyst", "data_analyst"]
)

st.divider()

resume_text = st.text_area(" Paste Resume Text Here", height=200)
job_description_text = st.text_area(" Paste Job Description Here", height=200)

if st.button("Analyze Match"):
    if resume_text and job_description_text:
        result = run_pipeline(resume_text, job_description_text, role)

        st.divider()
        st.subheader(" Analysis Result")

        st.write("###  Resume Skills Detected")
        st.write(", ".join(result["resume_skills"]))

        st.write("###  Job Skills Required")
        st.write(", ".join(result["job_skills"]))

        st.write("###  Matched Skills")
        st.write(", ".join(result["matched_skills"]))

        st.metric(" Match Score", f"{result['match_score']} %")

    else:
        st.warning("Please paste both Resume and Job Description.")
