import requests
import os

def download_webpage(url):
    response = requests.get(url)
    response.raise_for_status()

    # abstract web name as pre-name
    filename_prefix = url.split("//")[-1].split("/")[0]
    # save file to desktop
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    filepath = os.path.join(desktop, f"{filename_prefix}_source.txt")

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(response.text)
    print(f"Saved source code to: {filepath}")

if __name__ == "__main__":
    url = "https://bugs.chromium.org/p/chromium/issues/detail?id=1485783"
    download_webpage(url)
