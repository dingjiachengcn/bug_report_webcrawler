import csv
import os
import re

# 设置根目录路径
root_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'

# 用来保存所有独特状态的集合
unique_statuses = set()

# 读取Bug IDs
with open('/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv', 'r') as ids_file:
    reader = csv.reader(ids_file)
    for row in reader:
        bug_id = row[0]
        file_path = os.path.join(root_dir, f'{bug_id}', f'{bug_id}all.txt')

        # 确保文件存在
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = file.read()

                # 使用正则表达式查找状态，状态紧跟在"Status:"之后
                statuses = re.findall(r'Status:</th>\s*<td class="">\s*(.*?)\s*<em>', content)
                for status in statuses:
                    # 添加到集合中以去除重复项
                    unique_statuses.add(status.strip())

# 写入到status_catch.txt文件
status_catch_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/status_catch.txt'
with open(status_catch_path, 'w') as status_catch_file:
    for status in unique_statuses:
        status_catch_file.write(f'{status}\n')

print("Completed extracting unique statuses.")
