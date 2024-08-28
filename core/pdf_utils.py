from pathlib import Path
from typing import Generator

from PyPDF2 import PdfReader


def get_pages_with_text(pdf_path: Path) -> Generator[str, None, None]:
    with open(pdf_path, "rb") as f:
        pdf = PdfReader(f)
        for page in pdf.pages:
            yield page.extract_text()
        return None
