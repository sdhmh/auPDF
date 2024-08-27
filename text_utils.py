from pathlib import Path
from typing import Generator
from dataclasses import dataclass, asdict, field

import pysbd
import spacy
from spacy.language import Language

@Language.component("pysbd")
def pysbd_sentence_boundaries(doc):
    seg = pysbd.Segmenter(language="en", clean=False, char_span=True)
    sents_char_spans = seg.segment(doc.text)
    char_spans = [doc.char_span(sent_span.start, sent_span.end) for sent_span in sents_char_spans]
    start_token_ids = [span[0].idx for span in char_spans if span is not None]
    for token in doc:
        token.is_sent_start = True if token.idx in start_token_ids else False
    return doc

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
class FullText:
    name: str
    lines: list[Line] = field(default_factory=list)

    def todict(self) -> dict[str, str | list[Line]]:
        for s in self.lines:
            for c in s.text_chunks:
                c.chunk_audio_path = str(c.chunk_audio_path) # ik this is a problem but it is a workaround
        return asdict(self)



def init_pysbd() -> Language:
    seg = pysbd.Segmenter(language='en', clean=True) # text is dirty, clean it up.
    nlp = spacy.blank('en')

    # add as a spacy pipeline component
    nlp.add_pipe("pysbd")

    return nlp


def pad_int(integer: int, padding: int) -> str:
    return str(integer).zfill(padding)

def clean_line(line: str) -> str | None:
    if line.strip() == "":
        return None
    return line

def split_line(raw_line: str) -> list[str]:
    nlp = init_pysbd()       #print(raw_line)
    return list( line.text for line in nlp(raw_line).sents )

def clean_text(text: Generator[str, None, None], identifier: str) -> FullText:
    processed_text = FullText(name=identifier)
    for line_no, line in enumerate(text,1):
        processed_line = Line(id=pad_int(line_no, 4), text_chunks=[])
        line = clean_line(line)
        if not line:
            continue
        line_chunks = split_line(line)
        for chunk_id, chunk in enumerate(line_chunks, 1):
            line_data = LineChunk(id=f"{pad_int(line_no, 4)}/{pad_int(chunk_id,3)}", chunk=chunk)
            processed_line.text_chunks.append(line_data)
        processed_text.lines.append(processed_line)
    return processed_text
