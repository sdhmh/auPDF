import json
from pathlib import Path

from .speech_utils import convert_to_audio
from .text_utils import clean_text


def parse_page(
    input_file: Path, output_file: Path, output_dir: Path | None = None
) -> None:
    identifier = input_file.stem

    if not output_dir:
        output_dir = "processed" / Path(identifier)

    with open(input_file, "r", encoding="utf-8") as testfile:
        texts = clean_text((test for test in testfile), identifier=identifier)
        texts.lines = [
            convert_to_audio(line, output_directory=output_dir / "audio")
            for line in texts.lines
        ]

    with open(output_dir / output_file, "w", encoding="utf-8") as jf:
        json.dump(texts.todict(), jf)
