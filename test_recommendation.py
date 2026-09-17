from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import load_skill_dictionary, extract_skills
from job_matcher import load_job_roles, match_resume_to_roles
from roadmap_generator import generate_roadmap


# Resume file
file_path = "sample_resumes/reume_prefree_new-compressed.pdf"


# Extract and clean resume
raw_text = extract_resume_text(file_path)
cleaned_resume = clean_text(raw_text)


# Extract resume skills
skill_dictionary = load_skill_dictionary()
resume_skills = extract_skills(
    cleaned_resume,
    skill_dictionary
)


# Load job roles
job_roles = load_job_roles()


# Match resume with all roles
results = match_resume_to_roles(
    resume_skills,
    job_roles
)


# Get the highest-ranked role
top_role = results[0]


print("\n========== TOP JOB RECOMMENDATION ==========\n")

print(f"Recommended Role: {top_role['role']}")
print(f"Skill Match Score: {top_role['score']}%")

print("\nMissing Skills:")

for skill in top_role["missing_skills"]:
    print(f"  ✗ {skill}")


# Generate learning roadmap
roadmap = generate_roadmap(
    top_role["missing_skills"]
)


print("\n========== LEARNING ROADMAP ==========\n")

for item in roadmap:

    print(f"Skill: {item['skill']}")
    print(f"Recommendation: {item['recommendation']}")
    print("-" * 50)