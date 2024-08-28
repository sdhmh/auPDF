from .text_utils import (
    FullPageText,
    Line,
    LineChunk,
    clean_text,
    pad_int,
    split_line,
)


def parse_page(page_text: str, id: str) -> FullPageText:
    """
    Parses a page of text into a FullPageText object.

    If the page is empty, returns FullPageText(id=id, lines=[])

    Params:
    -------

    :param page_text: The text of the page to be parsed.
    :param id: The id of the page

    Returns:
    -------
    FullPageText: the parsed page

    """
    processed_text = FullPageText(id=id)

    clean_page_text = clean_text(page_text)
    if not clean_page_text:
        return processed_text
    for line_no, line in enumerate(clean_page_text.splitlines(), 1):
        line_id = f"{id}/{pad_int(line_no, 4)}"
        processed_line = Line(id=line_id, text_chunks=[])
        line_chunks = split_line(line)
        for chunk_id, chunk in enumerate(line_chunks, 1):
            chunk_id = f"{line_id}/{pad_int(chunk_id,3)}"
            line_data = LineChunk(id=chunk_id, chunk=chunk)
            processed_line.text_chunks.append(line_data)
        processed_text.lines.append(processed_line)
    return processed_text
