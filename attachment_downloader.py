import os
import re
import requests
import uuid
import time

def extract_links_from_file(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        links = re.findall(r'href="([^"]+)"', content)
        return set(links)


def download_and_save_attachment(link, save_path):

    base_url = "https://bugs.chromium.org/p/chromium/issues/"
    url = base_url + link.replace("&amp;", "&")  # 将 &amp; 替换为 &
    response = requests.get(url)

    content_disposition = response.headers.get('content-disposition')
    if content_disposition and 'filename=' in content_disposition:
        file_name = re.findall('filename="([^"]+)"', content_disposition)[0]
    else:

        file_name = str(uuid.uuid4())
    with open(os.path.join(save_path, file_name), 'wb') as file:
        file.write(response.content)


def read_bug_ids_from_csv(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def remove_bug_id_from_csv(file_path, bug_id):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip() != bug_id:
                file.write(line)

#
# def main():
#     base_path = "/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport"
#     csv_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids (copy).csv'
#
#     # 从CSV文件中读取bug IDs
#     bug_ids = read_bug_ids_from_csv(csv_path)
#
#     # 只处理CSV文件中列出的文件夹
#     for bug_id in bug_ids:
#         folder_path = os.path.join(base_path, bug_id)
#         if os.path.isdir(folder_path):
#             txt_file = os.path.join(folder_path, f"{bug_id}copy.txt")
#
#             # 检查文件是否存在
#             if os.path.exists(txt_file):
#                 attachment_folder = os.path.join(folder_path, "attachment")
#
#                 # 创建 attachment 文件夹（如果尚未存在）
#                 if not os.path.exists(attachment_folder):
#                     os.makedirs(attachment_folder)
#
#                 # 从文件中提取链接
#                 links = extract_links_from_file(txt_file)
#
#                 # 下载并保存每个附件
#                 for link in links:
#                     download_and_save_attachment(link, attachment_folder)
#
#                 # 打印进度
#                 print(f"已完成处理文件夹: {bug_id}")
#
#                 # 从CSV文件中删除已处理的bug ID
#                 remove_bug_id_from_csv(csv_path, bug_id)
#
#
# if __name__ == '__main__':
#     main()


def process_bug_id(bug_id, base_path):
    folder_path = os.path.join(base_path, bug_id)
    if os.path.isdir(folder_path):
        txt_file = os.path.join(folder_path, f"{bug_id}copy.txt")


        if os.path.exists(txt_file):
            attachment_folder = os.path.join(folder_path, "attachment")


            if not os.path.exists(attachment_folder):
                os.makedirs(attachment_folder)


            links = extract_links_from_file(txt_file)


            for link in links:
                download_and_save_attachment(link, attachment_folder)


            print(f"已完成处理文件夹: {bug_id}")


def main():
    base_path = "/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport"
    csv_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids (copy).csv'

    while True:
        bug_ids = read_bug_ids_from_csv(csv_path)

        if not bug_ids:
            print("所有bug ID已处理完毕!")
            break

        for bug_id in bug_ids:
            try:
                process_bug_id(bug_id, base_path)

                remove_bug_id_from_csv(csv_path, bug_id)
            except Exception as e:
                print(f"处理bug ID {bug_id}时出现错误: {e}")
                time.sleep(5)
                break


if __name__ == '__main__':
    main()