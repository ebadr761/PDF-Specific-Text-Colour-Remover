import fitz  # PyMuPDF

def remove_blue_text(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)
    
    for page in doc:
        text_instances = page.get_text("dict")["blocks"]
        
        for block in text_instances:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        # Convert integer color to RGB
                        # 0 is usually black. Blue is often 255 (0,0,255)
                        # We target anything that isn't black (0)
                        if span["color"] != 0: 
                            page.add_redact_annot(span["bbox"], fill=(1, 1, 1)) # Cover with white
        
        page.apply_redactions()
    
    doc.save(output_pdf)
    print(f"Done! Saved to {output_pdf}")

remove_blue_text("Final Practice - Solution.pdf", "cleaned_exam.pdf") # After adding your files to this directory, edit this line accordingly