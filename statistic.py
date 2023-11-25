import csv
import re
import os
from datetime import datetime

# 文件夹路径
bug_report_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
ids_file_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
output_csv = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/unique_assigned_counts.csv'

# 正则表达式模式
assigned_status_pattern = re.compile(
    r'Status:<strong>.*?</strong>\s*Assigned.*?<chops-timestamp title="(.*?)(?:\s*\(\d+\s*days? ago\))?"></chops-timestamp>',
    re.DOTALL
)

with open(output_csv, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Bug ID", "Unique Assigned Timestamps Count"])

    with open(ids_file_path, 'r') as ids_file:
        csv_reader = csv.reader(ids_file)
        for row in csv_reader:
            bug_id = row[0]
            file_path = os.path.join(bug_report_dir, f'{bug_id}/{bug_id}all.txt')

            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                assigned_timestamps = set(assigned_status_pattern.findall(content))
                csv_writer.writerow([bug_id, len(assigned_timestamps)])

print(f"Unique assigned timestamps count data saved to {output_csv}")
