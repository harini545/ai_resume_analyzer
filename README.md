\# AI Resume Analyzer and Job Recommendation System



An NLP-based application that analyzes resumes and evaluates how well they match different software and technology job roles.



\## Features



\- Upload resumes in PDF or DOCX format

\- Extract resume text using PDF parsing and OCR

\- Clean and normalize extracted text

\- Automatically identify technical skills

\- Detect major resume sections

\- Calculate resume completeness

\- Compare resumes against multiple job roles

\- Calculate skill-based match scores

\- Calculate TF-IDF similarity

\- Calculate semantic similarity using Sentence Transformers

\- Generate a combined job-role match score

\- Recommend top job roles

\- Identify missing skills

\- Generate a learning roadmap for missing skills

\- Interactive Streamlit dashboard



\## Job Roles



The current system supports:



\- Software Engineer

\- Backend Developer

\- Frontend Developer

\- Data Analyst

\- Machine Learning Engineer

\- AI Engineer



\## Technologies Used



\- Python

\- Streamlit

\- Pandas

\- NumPy

\- Scikit-learn

\- Sentence Transformers

\- PyPDF

\- python-docx

\- Tesseract OCR

\- pdf2image

\- Git \& GitHub



\## Matching Approach



The system combines three signals:



1\. \*\*Skill Matching\*\* – compares detected resume skills with required job skills.

2\. \*\*TF-IDF Similarity\*\* – measures textual similarity between the resume and job description.

3\. \*\*Semantic Similarity\*\* – uses Sentence Transformers to understand similarity between resume content and job requirements.



The final match score currently uses:



\- Skill Score: 50%

\- TF-IDF Score: 20%

\- Semantic Score: 30%



\## Project Structure



```text

ai\_resume\_analyzer/

│

├── app.py

├── resume\_parser.py

├── text\_cleaner.py

├── skill\_extractor.py

├── section\_detector.py

├── resume\_analyzer.py

├── resume\_score.py

├── job\_matcher.py

├── tfidf\_matcher.py

├── semantic\_matcher.py

├── combined\_matcher.py

├── roadmap\_generator.py

│

├── data/

│   ├── job\_roles.csv

│   └── skill\_dictionary.csv

│

├── sample\_resumes/

│

├── tests/

│

├── requirements.txt

├── .gitignore

└── README.md

