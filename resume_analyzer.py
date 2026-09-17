import re


def count_projects(text):
    """
    Estimate the number of projects from the Projects section.
    """

    text_lower = text.lower()

    match = re.search(
        r"\bprojects?\b(.*?)(?=\bcertifications?\b|\bskills?\b|$)",
        text_lower,
        re.DOTALL
    )

    if not match:
        return 0

    project_section = match.group(1).strip()

    # Common project-title patterns
    project_keywords = [
        "translator",
        "chatbot",
        "detection",
        "recognition",
        "application",
        "system",
        "platform",
        "website"
    ]

    detected = set()

    for keyword in project_keywords:
        if re.search(r"\b" + re.escape(keyword) + r"\b", project_section):
            detected.add(keyword)

    # Each distinct project-related concept is treated as evidence.
    return len(detected)
def detect_experience(text):
    """
    Detect whether actual internship or work experience
    is present in the resume.
    """

    text_lower = text.lower()

    # Look for common indicators of actual experience
    experience_keywords = [
        "intern",
        "internship",
        "worked at",
        "working at",
        "software developer",
        "software engineer",
        "developer intern",
        "developer",
        "engineer",
        "company",
        "organization",
        "responsibilities",
        "job role"
    ]

    for keyword in experience_keywords:
        if re.search(
            r"(?<![a-z])" + re.escape(keyword) + r"(?![a-z])",
            text_lower
        ):
            return True

    return False
def count_certifications(text):
    """
    Estimate the number of certification entries
    in the Certifications section.
    """

    text_lower = text.lower()

    match = re.search(
        r"\bcertifications?\b(.*?)(?=\bskills?\b|$)",
        text_lower,
        re.DOTALL
    )

    if not match:
        return 0

    certification_section = match.group(1).strip()

    # Split certification entries using common separators
    entries = re.split(
        r"\s{2,}|\n|(?=\b(?:aws|amazon|google|microsoft|nptel|coursera|forage)\b)",
        certification_section
    )

    certification_keywords = [
        "certificate",
        "certification",
        "aws",
        "google",
        "microsoft",
        "nptel",
        "coursera",
        "forage",
        "prompt engineering"
    ]

    detected_entries = []

    for entry in entries:
        entry = entry.strip()

        if not entry:
            continue

        if any(
            keyword in entry
            for keyword in certification_keywords
        ):
            detected_entries.append(entry)

    return len(detected_entries)