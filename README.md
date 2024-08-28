# auPDF

AuPDF is a simple PDF server built using Python and FastAPI which provides an API to convert PDFs to audio and server them.

> auPDF is still in early stages of development and is not yet ready for production use.

## Roadmap

- [x] Basic Functionality (parsing PDFs, converting to audio)
- [ ] Basic API
- [ ] Basic UI

## Technologies

- FastAPI
- PyPDF2 (to extract text from PDFs)
- spacy (to convert large chunk of text to smaller chunks)

More technologies will be added as the project progresses.

## Usage

### Installation

The base version of python used in this project is `3.12`.

Installing dependencies in a virtual environment is recommended.

On Unix-based systems, you can create a virtual environment using the following commands:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, you can create a virtual environment (Command Prompt) using the following commands:

```cmd
python -m venv .venv
call .\.venv\Scripts\activate
```

Install the dependencies in the virtual environment:
```bash
pip install -r requirements.txt
```

### using auPDF

For now, auPDF doesn't have an API or UI to interact with as it is barebones.

To test it, the `convert_pdf.py` file contains the necessary code to convert a PDF to audio.

You can use it by running the following command:

```bash
python `convert_pdf.py` -i <input_file> -o <output_folder_name>
```

A new folder with the name `processed` will be created inside which the output folder will reside.

It will have the necessary json containing the text of the page and the audio files in their respective folders.

> This guide will soon be updated with a proper API and UI.
> For now, you can use it as a standalone tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
