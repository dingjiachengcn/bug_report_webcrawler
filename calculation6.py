import csv
import re
from datetime import datetime
import os

# 文件夹路径
bug_report_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
ids_file_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
output_csv = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bug_duration (3rd copy).csv'

# 正则表达式模式
assigned_status_pattern = re.compile(
    r'Status:<strong>.*?</strong>\s*Assigned.*?<chops-timestamp title="(.*?)(?:\s*\(\d+\s*days? ago\))?"></chops-timestamp>',
    re.DOTALL
)

# 准备写入CSV文件
with open(output_csv, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Bug ID", "Last Assigned Time"])

    with open(ids_file_path, 'r') as ids_file:
        csv_reader = csv.reader(ids_file)
        for row in csv_reader:
            bug_id = row[0]
            file_path = os.path.join(bug_report_dir, f'{bug_id}/{bug_id}all.txt')

            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                assigned_times = assigned_status_pattern.findall(content)
                if assigned_times:
                    last_assigned_time_str = max(assigned_times)
                    last_assigned_time = datetime.strptime(last_assigned_time_str, '%a, %b %d, %Y, %I:%M %p %Z')
                    last_assigned_time_str = last_assigned_time.strftime('%Y-%m-%d %H:%M:%S')
                    csv_writer.writerow([bug_id, last_assigned_time_str])

print(f"Updated bug duration data saved to {output_csv}")
