from pathlib import Path

from PyPDF2 import PdfReader


def get_pages_with_text(pdf_path: Path) -> list[str]:
    with open(pdf_path, "rb") as f:
        pdf = PdfReader(f)
        pages = []
        for page in pdf.pages:
            pages.append(page.extract_text())
        return pages
