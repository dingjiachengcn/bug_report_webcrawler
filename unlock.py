import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# def get_all_content_from_shadow_roots(driver):
#     # 定义JavaScript函数以递归获取shadow DOM内容
#     script = '''
#     function getShadowContent(element) {
#         let content = element.outerHTML || "";
#         if (element.shadowRoot) {
#             content += Array.from(element.shadowRoot.children).map(child => getShadowContent(child)).join("");
#         }
#         return content;
#     }
#     return getShadowContent(document.body);
#     '''
#
#     # 使用execute_script执行上述JavaScript代码
#     return driver.execute_script(script)
#
# def recursive_unlock_and_get_content(driver, element):
#     get_shadow_root_js = "return arguments[0].shadowRoot || arguments[0];"
#     outerHTML_js = "return arguments[0].outerHTML;"
#
#     shadow_root = driver.execute_script(get_shadow_root_js, element)
#
#     if shadow_root == element:  # 没有更多的shadow root
#         return driver.execute_script(outerHTML_js, element)
#
#     # 递归进入shadow root
#     child_content = recursive_unlock_and_get_content(driver, shadow_root)
#     element_content = driver.execute_script(outerHTML_js, element)
#
#     # 由于element_content还包含了shadow_root的内容占位符，我们需要将这个占位符替换为实际的child_content
#     return element_content.replace("<slot></slot>", child_content)
#
#
# def recursive_shadow_dom_extraction(driver, element):
#     content = ""
#     try:
#         # 试图获取shadow root
#         shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
#     except:
#         shadow_root = None
#
#     # 如果shadow root存在，获取其所有子元素的内容
#     if shadow_root:
#         children = driver.execute_script('return arguments[0].children', shadow_root)
#         for child in children:
#             content += recursive_shadow_dom_extraction(driver, child)
#     else:
#         content = element.get_attribute('outerHTML')
#         children = element.find_elements(By.XPATH, './*')
#         for child in children:
#             content += recursive_shadow_dom_extraction(driver, child)
#
#     return content
#
# def unlock_all_shadow_roots(driver):
#     # 初始化JS函数
#     get_shadow_root_js = """
#         return arguments[0].shadowRoot;
#     """
#
#     # 从外层的<body>标签开始
#     current_element = driver.find_element(By.TAG_NAME, 'body')
#
#     # 循环解锁每一个shadow root
#     while current_element:
#         shadow_root = driver.execute_script(get_shadow_root_js, current_element)
#         if not shadow_root:
#             break
#         current_element = shadow_root
#
#     return current_element  # 返回内部最深层次的shadow root的内容
#
# def extract_shadow_content(driver, element):
#     shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
#     if not shadow_root:
#         return element.get_attribute('outerHTML')
#     else:
#         children = driver.execute_script('return arguments[0].childNodes', shadow_root)
#         content = []
#         for child in children:
#             content.append(extract_shadow_content(driver, child))
#         return "".join(content)

def get_shadow_content(driver, element):
    script = """
        const getDeepShadowContent = (elem) => {
            let content = [];
            if (elem.shadowRoot) {
                elem.shadowRoot.childNodes.forEach(child => {
                    content.push(getDeepShadowContent(child));
                });
            } else {
                content.push(elem.outerHTML || elem.textContent);
            }
            return content.join('');
        };
        return getDeepShadowContent(arguments[0]);
    """
    return driver.execute_script(script, element)


def fetch_and_save_html(url, folder_path, id_):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    with webdriver.Chrome(options=options) as driver:
        driver.get(url)
        sleep(10)  # 让页面完全加载

        # 首先，捕获常规DOM的内容
        regular_dom_content = driver.page_source

        # 接着，尝试从所有页面元素中获取shadow content
        all_elements = driver.find_elements(By.XPATH, "//*")
        shadow_contents = []

        for element in all_elements:
            try:
                shadow_content = get_shadow_content(driver, element)
                if shadow_content:
                    shadow_contents.append(shadow_content)
            except Exception as e:
                print(f"Error fetching shadow content for element: {e}")

        # 整合常规DOM内容和Shadow DOM内容
        all_content = regular_dom_content + "\n\n" + "\n".join(shadow_contents)

        with open(os.path.join(folder_path, f'{id_}11.txt'), 'w', encoding='utf-8') as f:
            f.write(all_content)


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
        print(f"Saved content for {id_} in {folder_path_for_id}/{id_}11.txt")

if __name__ == '__main__':
    main()
