#by prof. Zhihao Yao.


from html.parser import HTMLParser

# Define a custom HTML parser that will extract hyperlinks
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []  # To store the extracted hyperlinks

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    self.links.append(attr[1])

# Load your HTML file
with open('sample.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create the HTML parser
parser = MyHTMLParser()

# Feed the HTML content to the parser
parser.feed(html_content)

# Get the list of hyperlinks
hyperlinks = parser.links

# Print the hyperlinks
for link in hyperlinks:
    if "attachment" in link: print(link)
