import os
from selenium import webdriver
from time import sleep


def fetch_and_save_html(url, folder_path, id_):
    options = webdriver.ChromeOptions()
    options.headless = True  # 运行在无头模式，不显示浏览器窗口
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(
        f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    # 如果chrome driver不在你的PATH里，请修改以下路径
    # driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=options)
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        # 如果页面有延迟加载的内容，可以稍微等待一下
        sleep(5)
        html_content = driver.page_source

        # 保存的文件名为 {id_}01.txt
        with open(os.path.join(folder_path, f'{id_}01.txt'), 'w', encoding='utf-8') as f:
            f.write(html_content)

        return True

    except Exception as e:
        print(f"Failed to fetch {url}. Error: {e}")
        return False

    finally:
        driver.quit()


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

        success = fetch_and_save_html(url, folder_path_for_id, id_)
        if success:
            print(f"Saved content for {id_} in {folder_path_for_id}/{id_}01.txt")
        else:
            print(f"Failed to fetch content for {id_}")


if __name__ == '__main__':
    main()

