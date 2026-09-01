import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


@st.cache_resource
def load_model():
    """Load the NLP model once and reuse it."""
    return SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(resume_text, job_description):
    """
    Calculate semantic similarity between resume and job description.
    """

    model = load_model()

    resume_embedding = model.encode(
        [resume_text],
        convert_to_numpy=True
    )

    job_embedding = model.encode(
        [job_description],
        convert_to_numpy=True
    )

    similarity = cosine_similarity(
        resume_embedding,
        job_embedding
    )[0][0]

    return round(float(similarity) * 100, 2)


def calculate_final_score(
    semantic_score,
    matched_skills,
    jd_skills,
    experience_match
):
    """
    Calculate weighted resume-job match score.
    """

    if len(jd_skills) > 0:
        skill_score = (
            len(matched_skills) / len(jd_skills)
        ) * 100
    else:
        skill_score = 100

    if experience_match == "Good":
        experience_score = 100
    elif experience_match == "Moderate":
        experience_score = 60
    else:
        experience_score = 30

    final_score = (
        semantic_score * 0.60
        + skill_score * 0.30
        + experience_score * 0.10
    )

    return round(float(final_score), 2)