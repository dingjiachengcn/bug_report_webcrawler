import os
import csv
import re

def collect_categories(ids_file, base_dir, output_dir):
    # 用集合来存储不同的类别，以去除重复
    status_categories = set()
    labels_categories = set()

    # 读取所有的bug id
    with open(ids_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        bug_ids = [row[0] for row in csv_reader]

    for bug_id in bug_ids:
        comments_dir = os.path.join(base_dir, bug_id, "comments")
        if os.path.exists(comments_dir):
            for filename in os.listdir(comments_dir):
                file_path = os.path.join(comments_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    status_match = re.search(r'status: (.+)', content)
                    labels_match = re.search(r'labels: (.+)', content)
                    if status_match and status_match.group(1):
                        status_categories.add(status_match.group(1).strip())
                    if labels_match and labels_match.group(1):
                        labels_categories.add(labels_match.group(1).strip())

    # 保存status分类
    with open(os.path.join(output_dir, 'status_cat.txt'), 'w', encoding='utf-8') as file:
        for category in status_categories:
            file.write(category + '\n')

    # 保存labels分类
    with open(os.path.join(output_dir, 'labels_cat.txt'), 'w', encoding='utf-8') as file:
        for category in labels_categories:
            file.write(category + '\n')

    print("Category collection complete.")

if __name__ == "__main__":
    ids_file = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
    base_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
    output_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler'
    collect_categories(ids_file, base_dir, output_dir)
