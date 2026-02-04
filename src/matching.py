# src/matching.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(resume_text: str, jd_text: str) -> float:
    """
    Computes similarity score between a resume and a job description.

    Returns a percentage (0.0 - 100.0). If either input is empty or
    cannot be vectorized, returns 0.0.
    """

    if resume_text is None or jd_text is None:
        return 0.0

    resume_text = str(resume_text).strip()
    jd_text = str(jd_text).strip()

    if not resume_text or not jd_text:
        return 0.0

    documents = [resume_text, jd_text]

    vectorizer = TfidfVectorizer()
    try:
        tfidf_matrix = vectorizer.fit_transform(documents)
    except ValueError:
        # e.g., empty vocabulary when only stop words present
        return 0.0

    if tfidf_matrix.shape[0] < 2:
        return 0.0

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return float(similarity[0][0]) * 100.0  # percentage
