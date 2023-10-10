import os
import requests
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href" and "attachment" in attr[1]:
                    self.links.append(attr[1])


def download_file(url, folder):
    response = requests.get(url, stream=True)
    filename = os.path.join(folder, url.split('/')[-1])
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)


def main():
    root_folder = "/Users/jiachengding/PycharmProjects/bug_report_webcrawler/bugreport"

    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)

        # Ensure we're dealing with folders only and ignore any other files
        if not os.path.isdir(folder_path):
            continue

        txt_file_path = os.path.join(folder_path, f"{folder_name}.txt")

        if not os.path.exists(txt_file_path):
            print(f"File {txt_file_path} does not exist!")
            continue

        # Read and parse the HTML content
        with open(txt_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        parser = MyHTMLParser()
        parser.feed(content)

        # Download each attachment
        for link in parser.links:
            download_file(link, folder_path)
            print(f"Downloaded {link} to {folder_path}")


if __name__ == '__main__':
    main()
