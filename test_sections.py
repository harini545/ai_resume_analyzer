from resume_parser import extract_resume_text
from text_cleaner import clean_text
from section_detector import detect_sections


file_path = "sample_resumes/reume_prefree_new-compressed.pdf"

raw_text = extract_resume_text(file_path)

cleaned_text = clean_text(raw_text)

sections = detect_sections(cleaned_text)

print("\n----- SECTIONS DETECTED -----")

for section, found in sections.items():
    status = "✓ Found" if found else "✗ Not Found"
    print(f"{section.title()}: {status}")