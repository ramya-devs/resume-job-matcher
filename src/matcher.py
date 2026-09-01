from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(resume_text, job_description):
    """
    Calculate semantic similarity between resume and job description.
    """

    resume_embedding = model.encode([resume_text])
    job_embedding = model.encode([job_description])

    similarity = cosine_similarity(
        resume_embedding,
        job_embedding
    )[0][0]

    return float(round(float(similarity) * 100, 2))


def calculate_final_score(
    semantic_score,
    matched_skills,
    jd_skills,
    experience_match
):
    """
    Calculate weighted resume-job match score.
    """

    # Skill score
    if len(jd_skills) > 0:
        skill_score = (
            len(matched_skills) / len(jd_skills)
        ) * 100
    else:
        skill_score = 100

    # Experience score
    if experience_match == "Good":
        experience_score = 100
    elif experience_match == "Moderate":
        experience_score = 60
    else:
        experience_score = 30

    # Weighted final score
    final_score = (
        semantic_score * 0.60
        + skill_score * 0.30
        + experience_score * 0.10
    )

    return float(round(final_score, 2))