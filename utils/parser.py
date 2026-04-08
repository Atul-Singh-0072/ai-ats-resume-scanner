from PyPDF2 import PdfReader
import docx

def extract_text(file):
    text = ""

    if file.filename.endswith(".pdf"):
        reader = PdfReader(file)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content

    elif file.filename.endswith(".docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    return text