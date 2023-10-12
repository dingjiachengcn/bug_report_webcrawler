#by prof. Zhihao Yao.

from html.parser import HTMLParser

# Define a custom HTML parser that will extract plain text
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []  # To store the extracted plain text
        self.skip_tags = ["script", "style"]  # Tags to skip

    def handle_data(self, data):
        self.text.append(data)

    def handle_starttag(self, tag, attrs):
        if tag not in self.skip_tags:
            self.text.append(" ")  # Add space before non-skipped tags

    def handle_endtag(self, tag):
        if tag not in self.skip_tags:
            self.text.append(" ")  # Add space after non-skipped tags

# Load your HTML file
with open('sample.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create the HTML parser
parser = MyHTMLParser()

# Feed the HTML content to the parser
parser.feed(html_content)

# Get the plain text
plain_text = ''.join(parser.text)

# Print or save the plain text
with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(plain_text)

print(plain_text)