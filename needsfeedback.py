import csv
import re
import os

# 文件夹路径
bug_report_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
ids_file_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'

# 正则表达式模式
needs_feedback_pattern = re.compile(r'-Needs-Feedback')

# 读取Bug IDs
with open(ids_file_path, 'r') as ids_file:
    csv_reader = csv.reader(ids_file)
    for row in csv_reader:
        bug_id = row[0]
        file_path = os.path.join(bug_report_dir, f'{bug_id}/{bug_id}all.txt')

        # 确保文件存在
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 检查是否存在-Needs-Feedback标签
            if needs_feedback_pattern.search(content):
                print(bug_id)

print("Finished searching for -Needs-Feedback tags in bugs.")
