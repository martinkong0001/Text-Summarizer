from .parser import Parser
from docx import Document as docx_document
import os

class Docx_Parser(Parser):
    def parse(self):
        # Use docx module to extract text from DOCX
        doc = docx_document(self.input_file)
        
        # Extract each paragraph into a list
        all_paragraphs = []
        for para in doc.paragraphs:
            encoded_para = para.text.encode("ascii", "ignore")
            decoded_para = encoded_para.decode("ascii", "ignore")
            all_paragraphs.append(decoded_para)

        # Join all paragraphs into a single string
        extracted_text = os.linesep.join(all_paragraphs)
        return extracted_text
