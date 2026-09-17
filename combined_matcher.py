def calculate_final_score(
    skill_score,
    tfidf_score,
    semantic_score
):
    """
    Calculate the final resume-to-job-role match score.

    Weights:
    Skill matching    = 50%
    TF-IDF matching   = 20%
    Semantic matching = 30%
    """

    final_score = (
        skill_score * 0.50
        + tfidf_score * 0.20
        + semantic_score * 0.30
    )

    return round(final_score, 2)