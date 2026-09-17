from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import load_skill_dictionary, extract_skills


file_path = "sample_resumes/reume_prefree_new-compressed.pdf"

# Step 1: Extract
raw_text = extract_resume_text(file_path)

# Step 2: Clean
cleaned_text = clean_text(raw_text)
print("\n----- CLEANED RESUME TEXT -----")
print(cleaned_text)

# Step 3: Load skills
skill_dictionary = load_skill_dictionary()

# Step 4: Extract skills
skills = extract_skills(cleaned_text, skill_dictionary)

print("\n----- SKILLS FOUND -----")

for skill in skills:
    print("-", skill)