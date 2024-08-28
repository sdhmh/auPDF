import json
from argparse import ArgumentParser
from dataclasses import asdict
from pathlib import Path

import core
from core.text_utils import pad_int

args = ArgumentParser(
    description="Convert PDF to audio file using auPDFs default conversion method"
)

args.add_argument("-i", "--input", help="The input file (PDF)", required=True)
args.add_argument(
    "-o",
    "--output",
    dest="output_identifier",
    help="The output folder (unique identifier)",
    required=True,
)


def main(input: Path, identifier: str, output_path: Path | None = None):
    pages = core.get_pages_with_text(input)
    if not output_path:
        output_path = Path("processed") / identifier
    output_path.mkdir(parents=True, exist_ok=True)

    for c, page in enumerate(pages):
        full_page_text = core.parse_page(page, id=f"{identifier}/{pad_int(c, 4)}")
        for line in full_page_text.lines:
            for chunk in line.text_chunks:
                core.convert_to_audio(
                    chunk.chunk, Path("processed") / f"{chunk.id}.mp3", speed=0.8
                )
        (output_path / f"{pad_int(c, 4)}.json").write_text(
            json.dumps(full_page_text.todict())
        )


if __name__ == "__main__":
    args = args.parse_args()
    main(args.input, args.output_identifier)
