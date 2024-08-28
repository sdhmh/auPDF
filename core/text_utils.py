import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Generator

import spacy
from spacy.language import Language


@dataclass
class LineChunk:
    chunk: str
    id: str
    chunk_audio_path: Path | None | str = None


@dataclass
class Line:
    id: str
    text_chunks: list[LineChunk]


@dataclass
class FullPageText:
    id: str
    lines: list[Line] = field(default_factory=list)

    def todict(self) -> dict[str, str | list[Line]]:
        for s in self.lines:
            for c in s.text_chunks:
                c.chunk_audio_path = str(
                    c.chunk_audio_path
                )  # ik this is a problem but it is a workaround
        return asdict(self)


def pad_int(integer: int, padding: int) -> str:
    return str(integer).zfill(padding)


def clean_text(text: str) -> str | None:
    if text.strip() == "":
        return None

    text = re.sub(r"[\n\t\r]{2,}", " ", text).replace("\n", "")
    return text


def split_line(raw_line: str) -> list[str]:
    nlp = spacy.load("en_core_web_sm")  # print(raw_line)
    return list(line.text for line in nlp(raw_line).sents)
