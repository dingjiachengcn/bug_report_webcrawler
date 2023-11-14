import csv
import re
from datetime import datetime
import os

# 文件夹路径
bug_report_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
ids_file_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
output_csv = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bug_duration.csv'


# 正则表达式模式
report_time_pattern = re.compile(r'<chops-timestamp title="(.*?)(?:\s*\(\d+\s*days? ago\))?"></chops-timestamp>')
fixed_status_pattern = re.compile(
    r'Status:<strong>.*?</strong>\s*Fixed.*?<chops-timestamp title="(.*?)(?:\s*\(\d+\s*days? ago\))?"></chops-timestamp>',
    re.DOTALL
)

# 读取Bug IDs
with open(ids_file_path, 'r') as ids_file:
    csv_reader = csv.reader(ids_file)
    bug_ids = [row[0] for row in csv_reader]

# 准备写入CSV文件
with open(output_csv, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Bug ID", "Post Time", "Fixed Time", "Duration"])

    # 遍历每个bug ID
    for bug_id in bug_ids:
        file_path = os.path.join(bug_report_dir, f'{bug_id}/{bug_id}all.txt')

        # 确保文件存在
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 提取报告时间和修复时间
            report_time_match = report_time_pattern.search(content)
            fixed_status_match = fixed_status_pattern.search(content)

            if report_time_match:
                report_time = datetime.strptime(report_time_match.group(1), '%a, %b %d, %Y, %I:%M %p %Z')
                fixed_time_str = ""
                duration_str = ""

                if fixed_status_match:
                    fixed_time = datetime.strptime(fixed_status_match.group(1), '%a, %b %d, %Y, %I:%M %p %Z')
                    duration = fixed_time - report_time
                    fixed_time_str = fixed_time.strftime('%Y-%m-%d %H:%M:%S')
                    duration_str = str(duration)

                report_time_str = report_time.strftime('%Y-%m-%d %H:%M:%S')
                csv_writer.writerow([bug_id, report_time_str, fixed_time_str, duration_str])

print(f"Bug duration data saved to {output_csv}")
