SECTION_WEIGHTS = {
    "summary": 10,
    "education": 20,
    "experience": 20,
    "projects": 20,
    "skills": 20,
    "certifications": 10
}


def calculate_completeness_score(sections):
    total_score = 0

    for section, weight in SECTION_WEIGHTS.items():
        if sections.get(section, False):
            total_score += weight

    return total_score