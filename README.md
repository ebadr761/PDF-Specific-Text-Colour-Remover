Stop spoiling your practice exams! This tool automates the removal of colored "answer keys" from PDF documents. If your study resources have answers written directly below the questions in blue (or any other color), this script will detect that specific color and mask it with white, giving you a clean version ready for printing.

Here's How It Works:
The script scans every "span" of text in your PDF. If the text color matches the "solution color" defined in the script (and isn't the standard black text), it applies a white redaction box over it.

You will need Python installed and the PyMuPDF library:
Bash
pip install pymupdf

⚙️ Customization
If your answers aren't the standard blue, you can adjust the detection logic in the script:

Identify the color: Open your PDF in a browser or editor. Most "Blue" digital ink uses the integer code 255.

Edit the Script: * To remove everything that isn't black: Keep the condition if span["color"] != 0.

To remove a specific color: Change the condition to match your specific color code (e.g., if span["color"] == 16711680 for pure Red).

📖 Usage
Place your exam PDF in the same folder as the script.

Update the filename in the code and run the script and you should see a cleaned version. (When you clone this repo, make sure to remove my documents as you obviously don't need this practice exam, it's just to show it works.)
