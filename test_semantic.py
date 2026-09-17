from resume_parser import extract_resume_text
from text_cleaner import clean_text
from job_matcher import load_job_roles
from semantic_matcher import calculate_semantic_similarity


file_path = "sample_resumes/reume_prefree_new-compressed.pdf"

# Extract resume text
raw_text = extract_resume_text(file_path)

# Clean resume text
cleaned_resume = clean_text(raw_text)

# Load job roles
job_roles = load_job_roles()

results = []

# Compare resume with every job description
for _, row in job_roles.iterrows():

    score = calculate_semantic_similarity(
        cleaned_resume,
        row["job_description"]
    )

    results.append({
        "role": row["role"],
        "score": score
    })


# Sort from highest to lowest
results.sort(
    key=lambda x: x["score"],
    reverse=True
)


print("\n========== SEMANTIC JOB MATCH RESULTS ==========\n")

for result in results:
    print(f"Role: {result['role']}")
    print(f"Semantic Similarity: {result['score']}%")
    print("-" * 40)