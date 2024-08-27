import re
from pathlib import Path

from PyPDF2 import PdfReader


def get_pdf_text(pdf_path: Path) -> str:
    with open(pdf_path, "rb") as f:
        pdf = PdfReader(f)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        return text


def get_pdf_text_chunks(pdf_path: Path) -> list[str]:
    text = get_pdf_text(pdf_path)
    return re.split(r"(?<=[.!?])\s+", text)
