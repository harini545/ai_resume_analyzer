from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import load_skill_dictionary, extract_skills
from job_matcher import load_job_roles, calculate_all_match_scores


# Resume file
file_path = "sample_resumes/reume_prefree_new-compressed.pdf"


# Extract and clean resume
raw_text = extract_resume_text(file_path)
cleaned_resume = clean_text(raw_text)


# Extract skills
skill_dictionary = load_skill_dictionary()

resume_skills = extract_skills(
    cleaned_resume,
    skill_dictionary
)


# Load job roles
job_roles = load_job_roles()


# Calculate all matching scores
results = calculate_all_match_scores(
    cleaned_resume,
    resume_skills,
    job_roles
)


# Display results
print("\n========== UNIFIED MATCH RESULTS ==========\n")

for rank, result in enumerate(results, start=1):

    print(f"{rank}. {result['role']}")
    print(f"   Skill Score:    {result['skill_score']}%")
    print(f"   TF-IDF Score:   {result['tfidf_score']}%")
    print(f"   Semantic Score: {result['semantic_score']}%")
    print(f"   FINAL SCORE:    {result['final_score']}%")

    print("\n   Matched Skills:")
    for skill in result["matched_skills"]:
        print(f"      ✓ {skill}")

    print("\n   Missing Skills:")
    for skill in result["missing_skills"]:
        print(f"      ✗ {skill}")

    print("-" * 50)