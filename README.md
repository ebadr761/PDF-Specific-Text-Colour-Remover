# PDF Coloured Text Remover

**Need to remove all text of a particular colour from a PDF?** This tool automates the removal of colored text (answer keys in my case) from PDF documents which would be very tedious and require some weird online tool that will want you to make a account. If your study resources have answers written directly below the questions in blue (or any other color), this script detects that specific color and masks it with white, providing a clean version. I made this so I can do a practice test by printing it out without having the answers there.

Just make sure to edit the line that gets the PDF you want to change (I have it set to my practice exam but you should remove that and use your document) and once you have that inside the same directory as the python script, run the python file and you'll see a cleaned_exam.pdf which is that same PDF but without the type of coloured text you don't want.

---

## How It Works
The script scans every "span" of text in your PDF. If the text color matches the "solution color" defined in the script (and isn't the standard black text), it applies a white redaction box over that specific coordinate essentially erasing that colour of text from the document.

## Make sure to install PyMuPDF:

You will need **Python 3.x** installed. To handle the PDF processing, install the `PyMuPDF` library:

```bash
pip install pymupdf