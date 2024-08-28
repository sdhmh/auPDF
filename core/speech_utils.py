import os
from pathlib import Path
from typing import Literal

import openai

from .text_utils import FullPageText, Line

OPENAI_CLIENT = os.getenv(
    "OPENAI_CLIENT", "http://127.0.0.1:8000/v1"
)  # configured by default to use local openedai-speech
OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY", "sk-222222222"
)  # temp key for local models

client = openai.Client(api_key=OPENAI_API_KEY, base_url=OPENAI_CLIENT)


def convert_to_audio(
    text: str,
    output_path: Path,
    *,
    model: Literal["tts-1", "tts-1-hd"] = "tts-1",
    voice: Literal["alloy", "echo", "fable", "onyx", "nova", "shimmer"] = "alloy",
    response_format: Literal["mp3", "aac", "wav"] = "mp3",
    speed: float = 1.0,
):
    speaker = client.audio.speech.create(
        input=text,
        model=model,
        voice=voice,
        response_format=response_format,
        speed=speed,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    speaker.stream_to_file(output_path)
