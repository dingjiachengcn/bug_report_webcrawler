import csv
import os
import shutil

# 设置基本路径
base_comments_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/comments'
output_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/pocincludeincomment'

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 读取ids.csv文件中的所有ID
with open('/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv', 'r') as ids_file:
    csv_reader = csv.reader(ids_file)
    for row in csv_reader:
        bug_id = row[0].strip()  # 移除可能的空格
        combined_comments_file_path = os.path.join(base_comments_path, f'{bug_id}_comments_combined.txt')

        # 检查文件是否存在
        if os.path.isfile(combined_comments_file_path):
            with open(combined_comments_file_path, 'r') as file:
                content = file.read()
                if '#0' in content:
                    # 创建新文件的路径
                    new_file_path = os.path.join(output_dir, f'{bug_id}_comments_combined.txt')
                    # 复制文件
                    shutil.copy(combined_comments_file_path, new_file_path)

print("Completed copying files with '#0' in comments to the pocincludeincomment directory.")
