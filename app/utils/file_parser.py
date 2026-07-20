import pdfplumber
from docx import Document


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    """
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_text_from_docx(docx_path):
    """
    Extract text from a DOCX file.
    """
    doc = Document(docx_path)

    text = "\n".join(
        paragraph.text
        for paragraph in doc.paragraphs
    )

    return text