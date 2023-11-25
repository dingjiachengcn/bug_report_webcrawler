import csv
import json
import os
import re

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def parse_comments(comments_content):
    comments = []
    comment_pattern = re.compile(r'timestamp: (.*?)\nstatus: (.*?)\nowner: (.*?)\ncc: (.*?)\nlabels: (.*?)\ncomponents: (.*?)\n', re.DOTALL)
    matches = comment_pattern.findall(comments_content)

    for i, match in enumerate(matches):
        comment = {
            "id": i + 1,
            "timestamp": match[0].strip(),
            "status": match[1].strip(),
            "owner": match[2].strip(),
            "cc": match[3].strip(),
            "labels": match[4].strip(),
            "components": match[5].strip()
        }
        comments.append(comment)
    return comments

# 设置文件路径
ids_file_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
reports_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/report'

# 确保报告文件夹存在
os.makedirs(reports_dir, exist_ok=True)

# 读取所有bug IDs
with open(ids_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        bug_id = row[0]
        issue_file_path = f'/home/jiacheng/PycharmProjects/bug_report_webcrawler/issue/{bug_id}_c0_view.txt'
        comments_file_path = f'/home/jiacheng/PycharmProjects/bug_report_webcrawler/comments/{bug_id}_comments_combined.txt'
        report_file_path = os.path.join(reports_dir, f'{bug_id}.json')

        if os.path.exists(issue_file_path) and os.path.exists(comments_file_path):
            issue_content = read_file(issue_file_path)
            comments_content = read_file(comments_file_path)

            comments = parse_comments(comments_content)

            report_data = {
                bug_id: {
                    "issue": issue_content,
                    "comments": comments
                }
            }

            with open(report_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(report_data, json_file, indent=4)

print("All reports have been saved as JSON files.")
