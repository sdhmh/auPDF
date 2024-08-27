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
- spacy & pysbd (to convert large chunk of text to smaller and human-readable chunks)

More technologies will be added as the project progresses.

## Usage

### Installation

```bash
pip install -r requirements.txt
```

### using auPDF

For now, auPDF doesn't have an API or UI to interact with as it is barebones.

To test it, add an input file which already contian text. Reference it in the `core/page_utils.py` file.

You can use it by running the following command:

```bash
python core/page_utils.py
```

> This guide will soon be updated with a proper API and UI.
> For now, you can use it as a standalone tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
