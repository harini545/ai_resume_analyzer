from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import load_skill_dictionary, extract_skills
from job_matcher import load_job_roles, calculate_all_match_scores


file_path = "sample_resumes/reume_prefree_new-compressed.pdf"


# Extract resume text
raw_text = extract_resume_text(file_path)

# Clean resume text
cleaned_text = clean_text(raw_text)

# Extract skills
skill_dictionary = load_skill_dictionary()
resume_skills = extract_skills(
    cleaned_text,
    skill_dictionary
)

# Load job roles
job_roles = load_job_roles()

# Calculate all scores
results = calculate_all_match_scores(
    cleaned_text,
    resume_skills,
    job_roles
)


print("\n========== JOB MATCH RESULTS ==========\n")

for result in results:

    print(f"Role: {result['role']}")

    print(f"Skill Score: {result['skill_score']}%")
    print(f"TF-IDF Score: {result['tfidf_score']}%")
    print(f"Semantic Score: {result['semantic_score']}%")

    print(
        f"FINAL MATCH SCORE: "
        f"{result['final_score']}%"
    )

    print("Matched Skills:")

    for skill in result["matched_skills"]:
        print(f"  ✓ {skill}")

    print("Missing Skills:")

    for skill in result["missing_skills"]:
        print(f"  ✗ {skill}")

    print("-" * 40)