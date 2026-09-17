import re


def clean_text(text):
    """
    Clean raw resume text before further processing.
    """

    # Convert to lowercase
    text = text.lower()

    # Replace multiple spaces/newlines with one space
    text = re.sub(r"\s+", " ", text)

    # Remove unnecessary special characters
    text = re.sub(r"[^a-z0-9+#.\- ]", " ", text)

    # Remove extra spaces again
    text = re.sub(r"\s+", " ", text)

    return text.strip()