import os
import re

# 指定要遍历的目录
source_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport_copies'

# 定义要搜索的数字串
search_pattern = re.compile(r"99\.0\.4844\.51")

# 初始化一个列表来存储包含特定数字串的文件名
found_files = []

# 遍历目标目录中的所有文件
for root, dirs, files in os.walk(source_dir):
    for filename in files:
        file_path = os.path.join(root, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 检查文件内容中是否存在指定的数字串
        if search_pattern.search(content):
            found_files.append(filename)

# 打印找到的文件名
for filename in found_files:
    print(f"Found in file: {filename}")

print("Search completed.")
