from resume_parser import extract_resume_text

file_path = "sample_resumes/reume_prefree_new-compressed.pdf"

text = extract_resume_text(file_path)

print("----- EXTRACTED RESUME TEXT -----")
print(text)