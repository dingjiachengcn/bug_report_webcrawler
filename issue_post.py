import os
import csv

# 设置ids.csv文件和基础目录的路径
ids_file_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
base_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
issue_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/issue'

# 如果不存在，则创建新的issue目录
if not os.path.exists(issue_dir):
    os.makedirs(issue_dir)

# 读取所有bug IDs
with open(ids_file_path, newline='') as csvfile:
    bug_ids = list(csv.reader(csvfile))

# 遍历每个bug ID
for bug_id in bug_ids:
    # 检查每行是否确实只有一个元素
    if len(bug_id) == 1:
        bug_id = bug_id[0]  # 如果只有一个元素，直接获取
        # 构建原始issue文件的路径
        issue_file_path = os.path.join(base_dir, bug_id, 'issue', f'{bug_id}_c0_view.txt')
        # 构建目标路径
        target_file_path = os.path.join(issue_dir, f'{bug_id}_c0_view.txt')
        # 如果原始文件存在，复制到新的issue目录
        if os.path.exists(issue_file_path):
            with open(issue_file_path, 'r') as original_file:
                content = original_file.read()
            with open(target_file_path, 'w') as target_file:
                target_file.write(content)
        else:
            print(f'Issue file not found for bug ID {bug_id}')
    else:
        print(f'Unexpected number of elements in ids.csv row: {bug_id}')
