import re


SECTION_ALIASES = {
    "summary": [
        "summary",
        "profile",
        "profile summary",
        "objective",
        "career objective"
    ],
    "education": [
        "education",
        "academic background",
        "qualifications"
    ],
    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "internship",
        "internships"
    ],
    "projects": [
        "projects",
        "academic projects",
        "personal projects"
    ],
    "skills": [
        "skills",
        "technical skills",
        "skill set"
    ],
    "certifications": [
        "certifications",
        "certificates",
        "certification"
    ]
}


def detect_sections(text):
    """
    Detect common resume sections from cleaned resume text.
    """

    sections_found = {}

    for section, aliases in SECTION_ALIASES.items():

        for alias in aliases:

            pattern = r"\b" + re.escape(alias) + r"\b"

            if re.search(pattern, text.lower()):
                sections_found[section] = True
                break

        if section not in sections_found:
            sections_found[section] = False

    return sections_found