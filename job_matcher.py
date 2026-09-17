import pandas as pd


def load_job_roles(file_path="data/job_roles.csv"):
    return pd.read_csv(file_path)


def parse_required_skills(skill_string):
    return [
        skill.strip()
        for skill in skill_string.split(",")
        if skill.strip()
    ]


def parse_weights(weight_string):
    return [
        float(weight.strip())
        for weight in weight_string.split(",")
        if weight.strip()
    ]


def calculate_weighted_match(resume_skills, required_skills, weights):

    resume_skills_lower = {
        skill.lower()
        for skill in resume_skills
    }

    matched_skills = []
    missing_skills = []

    matched_weight = 0
    total_weight = sum(weights)

    for skill, weight in zip(required_skills, weights):

        if skill.lower() in resume_skills_lower:
            matched_skills.append(skill)
            matched_weight += weight
        else:
            missing_skills.append(skill)

    if total_weight == 0:
        score = 0
    else:
        score = (matched_weight / total_weight) * 100

    return {
        "score": round(score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }


def match_resume_to_roles(resume_skills, job_roles):

    results = []

    for _, row in job_roles.iterrows():

        required_skills = parse_required_skills(
            row["required_skills"]
        )

        weights = parse_weights(
            row["weights"]
        )

        match_result = calculate_weighted_match(
            resume_skills,
            required_skills,
            weights
        )

        results.append({
            "role": row["role"],
            "score": match_result["score"],
            "matched_skills": match_result["matched_skills"],
            "missing_skills": match_result["missing_skills"]
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results
from tfidf_matcher import calculate_tfidf_similarity
from semantic_matcher import calculate_semantic_similarity
from combined_matcher import calculate_final_score


def calculate_all_match_scores(
    resume_text,
    resume_skills,
    job_roles
):
    """
    Calculate skill, TF-IDF, semantic,
    and final scores for every job role.
    """

    results = []

    for _, row in job_roles.iterrows():

        # Required skills and weights
        required_skills = parse_required_skills(
            row["required_skills"]
        )

        weights = parse_weights(
            row["weights"]
        )

        # Skill matching
        skill_result = calculate_weighted_match(
            resume_skills,
            required_skills,
            weights
        )

        skill_score = skill_result["score"]

        # TF-IDF matching
        tfidf_score = calculate_tfidf_similarity(
            resume_text,
            row["job_description"]
        )

        # Semantic matching
        semantic_score = calculate_semantic_similarity(
            resume_text,
            row["job_description"]
        )

        # Combined score
        final_score = calculate_final_score(
            skill_score,
            tfidf_score,
            semantic_score
        )

        results.append({
            "role": row["role"],
            "skill_score": skill_score,
            "tfidf_score": tfidf_score,
            "semantic_score": semantic_score,
            "final_score": final_score,
            "matched_skills": skill_result["matched_skills"],
            "missing_skills": skill_result["missing_skills"]
        })

    # Rank using final score
    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return results