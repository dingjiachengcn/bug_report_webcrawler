import csv
import os
import shutil

# 设置基本路径
base_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
output_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/pocinclude'

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 读取ids.csv文件中的所有ID
with open('/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv', 'r') as ids_file:
    csv_reader = csv.reader(ids_file)
    for row in csv_reader:
        bug_id = row[0].strip()  # 移除可能的空格
        c0_file_path = os.path.join(base_path, bug_id, 'issue', f'{bug_id}_c0.txt')

        # 检查文件是否存在
        if os.path.isfile(c0_file_path):
            with open(c0_file_path, 'r') as file:
                content = file.read()
                if '#0' in content:
                    # 创建新文件的路径
                    new_file_path = os.path.join(output_dir, f'{bug_id}_c0.txt')
                    # 复制文件
                    shutil.copy(c0_file_path, new_file_path)

print("Completed copying files with '#0' to the pocinclude directory.")
