import os
from selenium import webdriver
from time import sleep

def fetch_and_save_html(url, folder_path, id_):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 使用无头模式
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    with webdriver.Chrome(options=options) as driver:
        driver.get(url)
        sleep(5)  # 让页面完全加载
        html_content = driver.page_source

        # 保存的文件名为 {id_}03.txt
        with open(os.path.join(folder_path, f'{id_}03.txt'), 'w', encoding='utf-8') as f:
            f.write(html_content)

def main():
    project_folder = "/Users/jiachengding/PycharmProjects/bug_report_webcrawler"
    bugreport_folder = os.path.join(project_folder, 'bugreport')
    urls_file_path = os.path.join(project_folder, 'ids_urls.txt')

    with open(urls_file_path, 'r') as f:
        urls = [url.strip() for url in f.readlines()]

    for url in urls:
        id_ = url.split("id=")[1].split("&")[0]
        folder_path_for_id = os.path.join(bugreport_folder, id_)

        if not os.path.exists(folder_path_for_id):
            os.makedirs(folder_path_for_id)

        fetch_and_save_html(url, folder_path_for_id, id_)
        print(f"Saved content for {id_} in {folder_path_for_id}/{id_}03.txt")

if __name__ == '__main__':
    main()
