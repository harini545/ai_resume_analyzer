from text_cleaner import clean_text

sample_text = """
Passionate about software development, Al applications,
and problem-solving.
Python, Streamlit, Sentence Transformers, Scikit-learn.
"""

cleaned = clean_text(sample_text)

print("----- CLEANED TEXT -----")
print(cleaned)