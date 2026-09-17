from pypdf import PdfReader
from docx import Document
from pdf2image import convert_from_path
import pytesseract


def extract_from_pdf(file_path):
    """Try normal PDF text extraction first."""

    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    # If normal extraction worked, return it
    if text.strip():
        return text

    # Otherwise use OCR
    print("No text layer found. Using OCR...")

    images = convert_from_path(file_path)

    ocr_text = ""

    for image in images:
        page_text = pytesseract.image_to_string(image)
        ocr_text += page_text + "\n"

    return ocr_text


def extract_from_docx(file_path):
    """Extract text from paragraphs and tables in a DOCX resume."""

    document = Document(file_path)

    text_parts = []

    # Extract normal paragraphs
    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text_parts.append(paragraph.text.strip())

    # Extract text from tables
    for table in document.tables:
        for row in table.rows:
            row_text = []

            for cell in row.cells:
                if cell.text.strip():
                    row_text.append(cell.text.strip())

            if row_text:
                text_parts.append(" | ".join(row_text))

    return "\n".join(text_parts)

def extract_resume_text(file_path):
    """Detect file type and extract resume text."""

    if file_path.lower().endswith(".pdf"):
        return extract_from_pdf(file_path)

    elif file_path.lower().endswith(".docx"):
        return extract_from_docx(file_path)

    else:
        raise ValueError("Only PDF and DOCX files are supported.")