def calculate_final_score(
    skill_score,
    tfidf_score,
    semantic_score,
    skill_weight=0.50,
    tfidf_weight=0.20,
    semantic_weight=0.30
):
    """
    Calculate the final resume-to-job-role match score.

    Default weights:
    Skill matching    = 50%
    TF-IDF matching   = 20%
    Semantic matching = 30%
    """

    total_weight = skill_weight + tfidf_weight + semantic_weight

    if total_weight == 0:
        return 0.0

    final_score = (
        skill_score * skill_weight
        + tfidf_score * tfidf_weight
        + semantic_score * semantic_weight
    ) / total_weight

    return round(final_score, 2)