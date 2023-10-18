import os
import re
import requests
import uuid


def extract_links_from_file(file_path):
    """从给定的文件中提取附件链接"""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # 使用正则表达式提取链接
        links = re.findall(r'href="([^"]+)"', content)
        return set(links)  # 使用 set 删除重复链接


def download_and_save_attachment(link, save_path):
    """下载附件并保存到给定的路径"""
    base_url = "https://bugs.chromium.org/p/chromium/issues/"
    url = base_url + link.replace("&amp;", "&")  # 将 &amp; 替换为 &
    response = requests.get(url)
    # 尝试从响应头部获取文件名
    content_disposition = response.headers.get('content-disposition')
    if content_disposition and 'filename=' in content_disposition:
        file_name = re.findall('filename="([^"]+)"', content_disposition)[0]
    else:
        # 如果获取失败，则生成一个唯一的文件名
        file_name = str(uuid.uuid4())
    with open(os.path.join(save_path, file_name), 'wb') as file:
        file.write(response.content)


def main():
    base_path = "/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport"

    # 遍历所有子文件夹
    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path):
            txt_file = os.path.join(folder_path, f"{folder}copy.txt")

            # 检查文件是否存在
            if os.path.exists(txt_file):
                attachment_folder = os.path.join(folder_path, "attachment")

                # 创建 attachment 文件夹（如果尚未存在）
                if not os.path.exists(attachment_folder):
                    os.makedirs(attachment_folder)

                # 从文件中提取链接
                links = extract_links_from_file(txt_file)

                # 下载并保存每个附件
                for link in links:
                    download_and_save_attachment(link, attachment_folder)

                # 打印进度
                print(f"已完成处理文件夹: {folder}")


if __name__ == '__main__':
    main()
