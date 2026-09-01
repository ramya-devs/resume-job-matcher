from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st


# ============================================================
# LOAD SENTENCE TRANSFORMER MODEL
# ============================================================

@st.cache_resource
def load_model():
    """
    Load the Sentence Transformer model once and reuse it.

    Streamlit cache prevents the model from being loaded again
    on every interaction or rerun.
    """
    return SentenceTransformer("all-MiniLM-L6-v2")


# ============================================================
# SEMANTIC SIMILARITY
# ============================================================

def calculate_similarity(resume_text, job_description):
    """
    Calculate semantic similarity between resume and job description.
    Returns a percentage from 0 to 100.
    """

    model = load_model()

    resume_text = resume_text or ""
    job_description = job_description or ""

    if not resume_text.strip() or not job_description.strip():
        return 0.0

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

    # Keep score between 0 and 100
    similarity_percentage = max(
        0.0,
        min(100.0, float(similarity) * 100)
    )

    return round(similarity_percentage, 2)


# ============================================================
# FINAL SCORE
# ============================================================

def calculate_final_score(
    semantic_score,
    matched_skills,
    jd_skills,
    experience_match
):
    """
    Calculate weighted resume-job match score.

    Weight:
        Semantic Similarity = 60%
        Skill Coverage      = 30%
        Experience          = 10%
    """

    # --------------------------------------------------------
    # Skill Score
    # --------------------------------------------------------

    if len(jd_skills) > 0:
        skill_score = (
            len(matched_skills) / len(jd_skills)
        ) * 100
    else:
        skill_score = 100.0

    # --------------------------------------------------------
    # Experience Score
    # --------------------------------------------------------

    if experience_match == "Good":
        experience_score = 100.0

    elif experience_match == "Moderate":
        experience_score = 60.0

    else:
        experience_score = 30.0

    # --------------------------------------------------------
    # Weighted Final Score
    # --------------------------------------------------------

    final_score = (
        float(semantic_score) * 0.60
        + float(skill_score) * 0.30
        + float(experience_score) * 0.10
    )

    # Keep score between 0 and 100
    final_score = max(
        0.0,
        min(100.0, final_score)
    )

    return round(final_score, 2)