from .parser import Parser
from tika import parser as tika_parser

class Pdf_Parser(Parser):
    def parse(self):
        # Use tika module to extract text from PDF
        raw_output = tika_parser.from_file(self.input_file)
        extracted_text = raw_output['content']
        return extracted_text
