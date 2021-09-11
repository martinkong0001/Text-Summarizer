# Text Summarizer
A text summarizer implemented using a graph-based Natural Language Processing algorithm called TextRank.

# Features
This text summarizer accepts inputs from a variety of file formats, such as .txt, .docx, .pdf, .jpg, .png, as well as website URLs.\
In order to extract text from image files (.jpg and .png), I have leveraged the power of Tesseract OCR and OpenCV library.\
In order to extract text from HTML documents and web pages, I have made use of the Beautiful Soup library.\
Once all the texts have been extracted from the given input document, they will be fed into the TextRank algorithm,\
which is a graph-based text summarization algorithm in the Natural Language Processing (NLP) field.

# Screenshots
Using this text summarizer, we can get a short summary of my professor's personal website :)
![Alt text](/../master/screenshots/WebsiteSummary.JPG)

Alternatively, we can also take a screenshot of the website, save it as a .jpg or .png file, and then feed this image file into the text summarizer.
![Alt text](/../master/screenshots/ImageSummary.JPG)
