import csv
import re
from datetime import datetime
import os

# 文件夹路径
bug_report_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
ids_file_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
output_csv = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bug_duration.csv'

# 正则表达式模式
wontfix_status_pattern = re.compile(
    r'Status:<strong>.*?</strong>\s*WontFix.*?<chops-timestamp title="(.*?)(?:\s*\(\d+\s*days? ago\))?"></chops-timestamp>',
    re.DOTALL
)

# 读取现有的bug duration数据
existing_data = {}
with open(output_csv, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # 跳过标题行
    for row in csv_reader:
        existing_data[row[0]] = row[1:]

# 准备写入CSV文件
with open(output_csv, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    # 更新标题行，添加新的列
    csv_writer.writerow(["Bug ID", "Post Time", "Fixed Time", "Duration", "Assigned Time", "Duration to Assign", "WontFix Time", "Duration to WontFix"])

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

                # 提取首次WontFix状态的时间
                wontfix_status_match = wontfix_status_pattern.search(content)

                wontfix_time_str = ""
                duration_to_wontfix_str = ""

                if wontfix_status_match:
                    wontfix_time = datetime.strptime(wontfix_status_match.group(1), '%a, %b %d, %Y, %I:%M %p %Z')
                    wontfix_time_str = wontfix_time.strftime('%Y-%m-%d %H:%M:%S')

                    # 计算到WontFix时间的持续时间
                    if bug_id in existing_data:
                        post_time_str = existing_data[bug_id][0]
                        post_time = datetime.strptime(post_time_str, '%Y-%m-%d %H:%M:%S')
                        duration_to_wontfix = wontfix_time - post_time
                        duration_to_wontfix_str = str(duration_to_wontfix)

                # 将信息写入CSV文件
                csv_writer.writerow([bug_id] + existing_data.get(bug_id, ["", "", "", "", ""]) + [wontfix_time_str, duration_to_wontfix_str])

print(f"Updated bug duration data with WontFix information saved to {output_csv}")
