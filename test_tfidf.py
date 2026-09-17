from resume_parser import extract_resume_text
from text_cleaner import clean_text
from job_matcher import load_job_roles
from tfidf_matcher import calculate_tfidf_similarity


# Resume file
file_path = "sample_resumes/reume_prefree_new-compressed.pdf"


# Extract and clean resume
raw_text = extract_resume_text(file_path)
cleaned_resume = clean_text(raw_text)


# Load job roles
job_roles = load_job_roles()


# Calculate TF-IDF similarity for every role
results = []

for _, row in job_roles.iterrows():

    job_description = row["job_description"]

    score = calculate_tfidf_similarity(
        cleaned_resume,
        job_description
    )

    results.append({
        "role": row["role"],
        "score": score
    })


# Sort highest to lowest
results.sort(
    key=lambda x: x["score"],
    reverse=True
)


# Display results
print("\n========== TF-IDF JOB MATCH RESULTS ==========\n")

for result in results:
    print(f"Role: {result['role']}")
    print(f"TF-IDF Similarity: {result['score']}%")
    print("-" * 40)