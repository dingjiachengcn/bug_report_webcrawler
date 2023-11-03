import os
import csv

# 设置基础路径
base_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport/'

# 读取ids.csv文件中的所有ID
with open('/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv', 'r') as ids_file:
    csv_reader = csv.reader(ids_file)
    empty_issues_directories = []  # 存储空issue目录的ID列表

    for row in csv_reader:
        bug_id = row[0].strip()  # 移除可能的空格
        issue_dir_path = os.path.join(base_path, bug_id, 'issue')

        # 检查目录是否存在并且为空
        if os.path.isdir(issue_dir_path) and not os.listdir(issue_dir_path):  # 目录存在且为空
            empty_issues_directories.append(bug_id)

# 打印出所有空issue目录的ID
for bug_id in empty_issues_directories:
    print(f'Issue directory for ID {bug_id} is empty.')

# 如果您还希望将这些ID写入到一个文件中，可以使用以下代码
empty_issues_dir_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/empty_issues_directories.txt'
with open(empty_issues_dir_path, 'w') as file:
    for bug_id in empty_issues_directories:
        file.write(f'{bug_id}\n')

print(f'Empty issues directories IDs have been written to {empty_issues_dir_path}')
