import os
import csv

def clean_attachments(base_dir, ids_file):
    # 读取所有的bug id
    with open(ids_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        bug_ids = [row[0] for row in csv_reader]

    for bug_id in bug_ids:
        attachments_path = os.path.join(base_dir, bug_id, 'attachment')

        # 检查目录是否存在
        if not os.path.isdir(attachments_path):
            print(f"Attachment directory for bug ID {bug_id} does not exist.")
            continue

        # 遍历目录中的文件
        for filename in os.listdir(attachments_path):
            if '.' not in filename:
                file_path = os.path.join(attachments_path, filename)
                # 删除没有扩展名的文件
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

        print(f"Cleaned attachments for bug ID {bug_id}.")

if __name__ == "__main__":
    base_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
    ids_file = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
    clean_attachments(base_dir, ids_file)
