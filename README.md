# PDF Coloured Text Remover

**Need to remove all text of a particular colour from a PDF?** This tool automates the removal of colored "answer keys" from PDF documents which would be very tedious and require some weird online tool that will want you to make a account. If your study resources have answers written directly below the questions in blue (or any other color), this script detects that specific color and masks it with white, providing a clean version. I made this so I can do a practice test by printing it out without having the answers there.

---

## How It Works
The script scans every "span" of text in your PDF. If the text color matches the "solution color" defined in the script (and isn't the standard black text), it applies a white redaction box over that specific coordinate.

## Make sure to install PyMuPDF:

You will need **Python 3.x** installed. To handle the PDF processing, install the `PyMuPDF` library:

```bash
pip install pymupdf