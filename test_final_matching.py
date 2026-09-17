from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import load_skill_dictionary, extract_skills
from job_matcher import load_job_roles, match_resume_to_roles
from tfidf_matcher import calculate_tfidf_similarity
from semantic_matcher import calculate_semantic_similarity
from combined_matcher import calculate_final_score


# Resume file
file_path = "sample_resumes/reume_prefree_new-compressed.pdf"


# --------------------------------------------------
# 1. Extract and clean resume
# --------------------------------------------------

raw_text = extract_resume_text(file_path)
cleaned_resume = clean_text(raw_text)


# --------------------------------------------------
# 2. Extract skills
# --------------------------------------------------

skill_dictionary = load_skill_dictionary()
resume_skills = extract_skills(
    cleaned_resume,
    skill_dictionary
)


# --------------------------------------------------
# 3. Load job roles
# --------------------------------------------------

job_roles = load_job_roles()


results = []


# --------------------------------------------------
# 4. Calculate all three scores
# --------------------------------------------------

for _, row in job_roles.iterrows():

    # Weighted skill matching
    skill_result = match_resume_to_roles(
        resume_skills,
        job_roles[job_roles["role"] == row["role"]]
    )[0]

    skill_score = skill_result["score"]

    # TF-IDF matching
    tfidf_score = calculate_tfidf_similarity(
        cleaned_resume,
        row["job_description"]
    )

    # Semantic matching
    semantic_score = calculate_semantic_similarity(
        cleaned_resume,
        row["job_description"]
    )

    # Final combined score
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


# --------------------------------------------------
# 5. Rank roles using final score
# --------------------------------------------------

results.sort(
    key=lambda x: x["final_score"],
    reverse=True
)


# --------------------------------------------------
# 6. Display results
# --------------------------------------------------

print("\n========== FINAL JOB MATCH RESULTS ==========\n")

for rank, result in enumerate(results, start=1):

    print(f"{rank}. {result['role']}")
    print(f"   Skill Score:     {result['skill_score']}%")
    print(f"   TF-IDF Score:    {result['tfidf_score']}%")
    print(f"   Semantic Score:  {result['semantic_score']}%")
    print(f"   FINAL SCORE:     {result['final_score']}%")

    print("\n   Matched Skills:")
    for skill in result["matched_skills"]:
        print(f"      ✓ {skill}")

    print("\n   Missing Skills:")
    for skill in result["missing_skills"]:
        print(f"      ✗ {skill}")

    print("-" * 50)