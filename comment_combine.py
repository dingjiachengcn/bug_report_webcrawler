import os


def combine_comments(base_dir, ids_file):
    # 读取所有的bug id
    with open(ids_file, mode='r', encoding='utf-8') as file:
        bug_ids = [line.strip().split(',')[0] for line in file]

    for bug_id in bug_ids:
        comments_dir = os.path.join(base_dir, bug_id, 'comments')
        combined_content = ""

        # 检查评论目录是否存在
        if not os.path.isdir(comments_dir):
            print(f"Comments directory for bug ID {bug_id} does not exist.")
            continue

        # 获取所有评论文件
        comment_files = [f for f in os.listdir(comments_dir) if f.startswith(bug_id) and f.endswith('.txt')]

        # 按照文件名排序确保顺序（如果需要）
        comment_files.sort()

        # 合并文件内容
        for filename in comment_files:
            file_path = os.path.join(comments_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as comment_file:
                combined_content += comment_file.read() + "\n"

        # 写入合并后的内容到新文件
        combined_file_path = os.path.join(comments_dir, f"{bug_id}_comment_combine.txt")
        with open(combined_file_path, 'w', encoding='utf-8') as combined_file:
            combined_file.write(combined_content)
        print(f"Combined comments for bug ID {bug_id} into {combined_file_path}")


if __name__ == "__main__":
    base_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
    ids_file = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
    combine_comments(base_dir, ids_file)
