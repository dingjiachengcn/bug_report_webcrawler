import re
import os
import csv

# 解析评论的函数
def parse_comment(comment_html):
    timestamp_match = re.search(r'<chops-timestamp title="([^"]+)">', comment_html)
    status_match = re.search(r'Status:<strong><!---->Status:</strong>\s*(.+?)\s*<br>', comment_html)
    owner_match = re.search(r'Owner:<strong><!---->Owner:</strong>\s*(.+?)\s*<br>', comment_html)
    cc_match = re.search(r'Cc:<strong><!---->Cc:</strong>\s*(.+?)\s*<br>', comment_html)
    labels_match = re.search(r'Labels:<strong><!---->Labels:</strong>\s*(.+?)\s*<br>', comment_html)
    components_match = re.search(r'<br>\s*<!---->\s*</div><br>\s*(.*?)\s*<div>', comment_html, re.DOTALL)

    # 提取数据，如果匹配失败则为空字符串
    comment_data = {
        "timestamp": timestamp_match.group(1) if timestamp_match else "",
        "status": status_match.group(1) if status_match else "",
        "owner": owner_match.group(1) if owner_match else "",
        "cc": cc_match.group(1) if cc_match else "",
        "labels": labels_match.group(1) if labels_match else "",
        "components": components_match.group(1).strip() if components_match else "",
    }

    return comment_data


# 从文件中提取评论数据的函数
def extract_comments_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    comments = re.split(r'Comment\s+\d+<', content)
    comments_data = []

    for i, comment_html in enumerate(comments[1:], start=1):  # 跳过第一个元素，它通常是空的
        comment_data = parse_comment(comment_html)
        if not comment_data['timestamp']:
            print(f"No timestamp found for comment {i}, skipping.")
            continue  # 如果没有时间戳，跳过当前评论
        comments_data.append(comment_data)

    return comments_data

# 主程序函数
def main():
    base_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
    ids_file = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'

    # 读取所有的ID
    with open(ids_file, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            bug_id = row[0]
            bug_folder_path = os.path.join(base_dir, bug_id)
            copy_file_path = os.path.join(bug_folder_path, f'{bug_id}copy.txt')

            # 检查相应的copy.txt文件是否存在
            if os.path.isfile(copy_file_path):
                comments_data = extract_comments_from_file(copy_file_path)
                # 处理每个评论数据
                comments_path = os.path.join(bug_folder_path, 'comments')
                os.makedirs(comments_path, exist_ok=True)

                for i, comment_data in enumerate(comments_data, start=1):
                    comment_filename = f"{bug_id}_comment_{i}.txt"
                    with open(os.path.join(comments_path, comment_filename), 'w') as comment_file:
                        for key, value in comment_data.items():
                            comment_file.write(f"{key}: {value}\n")
            else:
                print(f'文件 {copy_file_path} 不存在。')

# 程序入口点
if __name__ == "__main__":
    main()
