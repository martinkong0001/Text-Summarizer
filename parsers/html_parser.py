from .parser import Parser
import bs4
import urllib.request
import re

class Html_Parser(Parser):
    def is_tag_visible(self, html_element):
        # The following tags are not visible to the user
        if html_element.parent.name in ['meta', 'title', 'head', 'style', 'script', '[document]']:
            return False

        # Comments are not visible to the user either
        if isinstance(html_element, bs4.element.Comment):
            return False

        # Also remove white spaces and line breaks
        if re.match(r"[\s\r\n]+", str(html_element)):
            return False
        return True

    def extract_text_from_html(self, html):
        # Use beautiful soup to parse the html document
        soup = bs4.BeautifulSoup(html, 'html.parser')

        # Extract all texts from the html document
        all_texts = soup.findAll(text=True)

        # Remove all texts which are not visible to the user
        visible_texts = filter(self.is_tag_visible, all_texts)

        # Merge all visible texts into a single string
        joined_texts = u" ".join(t.strip() for t in visible_texts)
        return joined_texts

    def parse(self):
        html = urllib.request.urlopen(self.input_file).read()
        extracted_text = self.extract_text_from_html(html)
        return extracted_text
