import os
import requests
from bs4 import BeautifulSoup
from time import sleep


def fetch_and_save_html(url, folder_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        with open(os.path.join(folder_path, 'bugreport.html'), 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))
    else:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")
        return False

    # 为了避免频繁请求导致IP被封，我们在每次请求之间稍作暂停
    sleep(2)
    return True


def main():
    project_folder = "/Users/jiachengding/PycharmProjects/bug_report_webcrawler"
    bugreport_folder = os.path.join(project_folder, 'bugreport')
    urls_file_path = os.path.join(project_folder, 'ids_urls.txt')

    with open(urls_file_path, 'r') as f:
        urls = f.readlines()

    for url in urls:
        url = url.strip()
        id_ = url.split("id=")[1].split("&")[0]
        folder_path = os.path.join(bugreport_folder, id_)
        success = fetch_and_save_html(url, folder_path)
        if success:
            print(f"Saved content for {id_} in {folder_path}")
        else:
            print(f"Failed to fetch content for {id_}")


if __name__ == '__main__':
    main()
