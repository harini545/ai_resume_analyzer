import pandas as pd
import re


def load_skill_dictionary(file_path="data/skill_dictionary.csv"):
    return pd.read_csv(file_path)


# Common variations and OCR mistakes
SKILL_ALIASES = {
    "ml": "Machine Learning",
    "ai": "Artificial Intelligence",
    "dl": "Deep Learning",
    "nlp": "NLP",
    "genai": "Generative AI",
    "gen ai": "Generative AI",
    "llms": "LLM",
    "llm": "LLM",
    "rag": "RAG",

    "js": "JavaScript",
    "reactjs": "React",
    "react.js": "React",
    "nodejs": "Node.js",
    "node.js": "Node.js",

    "scikit learn": "Scikit-learn",
    "sklearn": "Scikit-learn",
    "sentence-transformers": "Sentence Transformers",

    "sql": "SQL",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",

    "rest": "REST API",
    "restful api": "REST API",
    "api development": "REST API",

    "ds": "Data Structures",
    "dsa": "Data Structures",
    "data structures and algorithms": "Data Structures",

    "gitlab": "Git",
    "version control": "Git",

    "aws cloud": "AWS",

    "grog": "Groq",
    "groq api": "Groq",
}
URL_SKILL_PATTERNS = {
    "github": "GitHub",
    "git hub": "GitHub",
    "github.com": "GitHub",
    "linkedin": "LinkedIn",
}

def normalize_skill(skill):
    return skill.strip().lower()


def extract_skills(text, skill_dictionary):
    text_lower = text.lower()

    # Common OCR corrections
    ocr_corrections = {
        " al ": " ai ",
        " grog ": " groq ",
        " scikit learn ": " scikit-learn ",
        " sentence transformers ": " sentence-transformers "
    }

    for wrong, correct in ocr_corrections.items():
        text_lower = text_lower.replace(wrong, correct)

    found_skills = []

    for skill in skill_dictionary["skill"]:
        skill_lower = normalize_skill(skill)

        # Special handling for one-letter skill "C"
        if skill_lower == "c":
            pattern = r"(?<![a-z])c(?![a-z])"
        else:
            pattern = r"(?<![a-z0-9+#.-])" + re.escape(skill_lower) + r"(?![a-z0-9+#.-])"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    # Check aliases
    for alias, standard_skill in SKILL_ALIASES.items():
        pattern = r"(?<![a-z0-9+#.-])" + re.escape(alias) + r"(?![a-z0-9+#.-])"

        if re.search(pattern, text_lower):
            if standard_skill in skill_dictionary["skill"].values:
                if standard_skill not in found_skills:
                    found_skills.append(standard_skill)

    # Detect skills from URLs and common resume text
    for pattern_text, standard_skill in URL_SKILL_PATTERNS.items():
        if pattern_text in text_lower:
            if standard_skill in skill_dictionary["skill"].values:
                if standard_skill not in found_skills:
                    found_skills.append(standard_skill)
    found_skills = list(dict.fromkeys(found_skills))
    return found_skills
    