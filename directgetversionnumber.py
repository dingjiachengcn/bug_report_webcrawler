import os
import csv
import re

# 文件夹路径
issue_folder = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/issue'
csv_file_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/token_count.csv'

# 正则表达式
bug_id_pattern = re.compile(r'(\d+)_c\d+_view\.txt')
version_pattern = re.compile(r'\b\d+\.\d+\.\d+\.\d+\b')  # 正则表达式，用于匹配版本号

# 读取 CSV 文件
updated_rows = []
with open(csv_file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    headers.extend(['Chromium Version', 'Version Found'])  # 添加新列
    updated_rows.append(headers)

    # 将 CSV 文件转换为字典便于更新
    rows_dict = {row[0]: row for row in reader}

version_count = 0  # 统计找到的版本号数量

# 遍历 issue 文件夹中的文件
for filename in os.listdir(issue_folder):
    match = bug_id_pattern.match(filename)
    if match:
        bug_id = match.group(1)
        with open(os.path.join(issue_folder, filename), 'r') as file:
            content = file.read()
            version_match = version_pattern.search(content)
            version_info = version_match.group(0) if version_match else ""
            if version_info:
                version_count += 1  # 更新找到版本号的计数
            # 更新 CSV 行
            if bug_id in rows_dict:
                rows_dict[bug_id].extend([version_info, 'Yes' if version_info else 'No'])

# 将更新后的数据写回 CSV 文件
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    for row in updated_rows:
        writer.writerow(row)
    for row in rows_dict.values():
        writer.writerow(row)

print(f"Updated CSV file with Chromium versions. Total versions found: {version_count}")
