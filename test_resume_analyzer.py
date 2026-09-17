from resume_parser import extract_resume_text
from text_cleaner import clean_text
from resume_analyzer import count_projects, detect_experience, count_certifications


file_path = "sample_resumes/reume_prefree_new-compressed.pdf"

raw_text = extract_resume_text(file_path)

cleaned_text = clean_text(raw_text)

project_count = count_projects(cleaned_text)
experience_found = detect_experience(cleaned_text)
certification_count = count_certifications(cleaned_text)

print("\n----- RESUME CONTENT ANALYSIS -----")
print(f"Estimated Projects: {project_count}")
print(f"Experience Section: {'Found' if experience_found else 'Not Found'}")
print(f"Certifications Detected: {certification_count}")