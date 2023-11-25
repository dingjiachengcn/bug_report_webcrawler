import csv
import shutil
import os

# 设置路径
source_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
ids_file_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
target_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport_copies'

# 确保目标目录存在
os.makedirs(target_dir, exist_ok=True)

# 读取Bug IDs
with open(ids_file_path, 'r') as ids_file:
    csv_reader = csv.reader(ids_file)
    for row in csv_reader:
        bug_id = row[0]
        source_file_path = os.path.join(source_dir, f'{bug_id}/{bug_id}all.txt')
        target_file_path = os.path.join(target_dir, f'{bug_id}all.txt')

        # 如果源文件存在，则复制它
        if os.path.exists(source_file_path):
            shutil.copyfile(source_file_path, target_file_path)
        else:
            print(f"Source file not found: {source_file_path}")

print("Completed copying all.txt files.")
