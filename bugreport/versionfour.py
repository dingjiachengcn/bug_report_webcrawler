import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def access_shadow_root(driver, element):
    return driver.execute_script('return arguments[0].shadowRoot', element)


def recursive_shadow_root_extraction(driver, element):
    # 检查元素是否有 shadow root
    js_check_shadow = 'return arguments[0].shadowRoot !== null;'
    has_shadow = driver.execute_script(js_check_shadow, element)

    # 如果没有 shadow root，返回元素的 outerHTML
    if not has_shadow:
        return element.get_attribute('outerHTML')

    # 获取 shadow root 的所有子元素
    js_get_children = '''
    let children = arguments[0].shadowRoot.querySelectorAll("*");
    return Array.from(children).map(e => e.outerHTML).join("");
    '''
    children_html = driver.execute_script(js_get_children, element)

    # 获取当前元素的 shadow root 的 outerHTML
    js_get_shadow_outerHTML = 'return arguments[0].shadowRoot.outerHTML;'
    shadow_outerHTML = driver.execute_script(js_get_shadow_outerHTML, element)

    # 检查 shadow_outerHTML 是否为 None，如果是，则将其设置为一个空字符串
    if shadow_outerHTML is None:
        shadow_outerHTML = ""

    # 返回整合后的内容
    return shadow_outerHTML + children_html


def fetch_and_save_html_and_attachments(url, folder_path, id_):
    options = webdriver.ChromeOptions()
    # 如果需要观察浏览器行为，可以注释掉下面的无头模式
    # options.add_argument('--headless')  # 使用无头模式
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    with webdriver.Chrome(options=options) as driver:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "mr-issue-header")))

        # 删除所有带有hidden属性的元素的hidden属性
        hidden_elements = driver.find_elements(By.XPATH, '//*[@hidden]')
        for element in hidden_elements:
            driver.execute_script("arguments[0].removeAttribute('hidden')", element)

        # 获取mr-issue-header的完整内容，包括其所有的shadow root
        issue_header = driver.find_element(By.TAG_NAME, "mr-issue-header")
        full_content = recursive_shadow_root_extraction(driver, issue_header)

        # 下载所有附件
        attachment_links = driver.find_elements(By.XPATH, '//a[@class="attachment-download"]')
        for link in attachment_links:
            href = link.get_attribute("href")
            driver.get(href)
            sleep(2)  # 等待文件下载完成

        html_content = driver.page_source

        # 保存的文件名为 {id_}03.txt
        with open(os.path.join(folder_path, f'{id_}05.txt'), 'w', encoding='utf-8') as f:
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

        fetch_and_save_html_and_attachments(url, folder_path_for_id, id_)
        print(f"Saved content for {id_} in {folder_path_for_id}/{id_}03.txt")


if __name__ == '__main__':
    main()
