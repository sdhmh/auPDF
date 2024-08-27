import os
from pathlib import Path

import openai

from text_utils import Line

OPENAI_CLIENT = os.getenv("OPENAI_CLIENT", "http://127.0.0.1:8000/v1") # configured by default to use local openedai-speech
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-222222222") # temp key for local models

client = openai.Client(api_key=OPENAI_API_KEY, base_url=OPENAI_CLIENT)

def convert_to_audio(line: Line, output_directory: Path | None = None) -> Line:
    if not output_directory:
        output_directory = Path("audio")
    for chunk in line.text_chunks:
        speaker = client.audio.speech.create(input=chunk.chunk, model="tts-1", voice="alloy", response_format="mp3", speed=.8)

        output_path = output_directory/(chunk.id + ".mp3")
        output_path.parent.mkdir(exist_ok=True, parents=True)

        speaker.stream_to_file(output_path)

        chunk.chunk_audio_path = output_path
    return line
