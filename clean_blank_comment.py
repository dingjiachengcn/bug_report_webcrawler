import os
import csv
import re

def clean_files(base_dir, ids_file):
    with open(ids_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            bug_id = row[0]
            comments_dir = os.path.join(base_dir, bug_id, "comments")
            if os.path.exists(comments_dir):
                # 匹配格式为 'bug_id_comment_number.txt' 的文件
                pattern = re.compile(rf"^{bug_id}_comment_\d+\.txt$")
                for file_name in filter(pattern.match, os.listdir(comments_dir)):
                    file_path = os.path.join(comments_dir, file_name)
                    with open(file_path, 'r') as f:
                        content = f.read()
                    # 检查除了timestamp以外的字段是否为空
                    fields = ['status', 'owner', 'cc', 'labels', 'components']
                    if all(re.search(rf"{field}:\s*$", content, re.MULTILINE) for field in fields):
                        os.remove(file_path)  # 删除文件
                        print(f"Deleted {file_path}")

# 定义基本目录和ID文件路径
base_directory = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
ids_csv_file = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'

# 调用函数开始清理
clean_files(base_directory, ids_csv_file)
