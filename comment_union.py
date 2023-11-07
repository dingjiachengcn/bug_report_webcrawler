import os
import csv
import re


# 读取每个评论文件的内容并检查是否包含至少一个非空字段
def is_comment_valid(content):
    fields = ['status', 'owner', 'cc', 'labels', 'components']
    for field in fields:
        if re.search(rf'{field}:\s*\S+', content):
            return True
    return False


def combine_comments(bug_id, comments_dir):
    comments_with_numbers = []
    for filename in os.listdir(comments_dir):
        match = re.search(r'(\d+)\.txt$', filename)
        if match:
            with open(os.path.join(comments_dir, filename), 'r') as file:
                content = file.read().strip()
                if is_comment_valid(content):
                    comment_number = int(match.group(1))
                    comments_with_numbers.append((comment_number, content))

    # Sort the comments based on the extracted numbers
    comments_with_numbers.sort(key=lambda x: x[0])

    # Write the sorted comments to the union file
    union_file_path = os.path.join(comments_dir, f'{bug_id}_union.txt')
    with open(union_file_path, 'w') as union_file:
        for _, comment in comments_with_numbers:
            union_file.write(comment + '\n\n')

    return union_file_path


def process_all_bugs(ids_file, base_dir):
    with open(ids_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        bug_ids = [row[0] for row in csv_reader]

    for bug_id in bug_ids:
        comments_dir = os.path.join(base_dir, bug_id, 'comments')
        if os.path.isdir(comments_dir):
            union_file = combine_comments(bug_id, comments_dir)
            print(f"Combined file created: {union_file}")
        else:
            print(f"Comments directory for bug ID {bug_id} does not exist.")


if __name__ == '__main__':
    ids_file_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
    base_comments_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'

    process_all_bugs(ids_file_path, base_comments_dir)
