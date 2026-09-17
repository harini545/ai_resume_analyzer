from section_detector import detect_sections
from resume_parser import extract_resume_text
from text_cleaner import clean_text
from resume_score import calculate_completeness_score


file_path = "sample_resumes/reume_prefree_new-compressed.pdf"

raw_text = extract_resume_text(file_path)

cleaned_text = clean_text(raw_text)

sections = detect_sections(cleaned_text)

score = calculate_completeness_score(sections)

print("\n----- RESUME COMPLETENESS -----")
print(f"Completeness Score: {score}%")