import os
import csv

# 设置基础路径和CSV文件路径
base_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler'
ids_csv_path = os.path.join(base_path, 'ids.csv')

# 创建存放所有合并评论文件的目录
combined_comments_dir = os.path.join(base_path, 'comments')
os.makedirs(combined_comments_dir, exist_ok=True)  # 如果目录不存在，则创建目录

# 读取所有bug ID
with open(ids_csv_path, 'r') as file:
    bug_ids = [row[0] for row in csv.reader(file) if row]  # 假设每行第一列是bug ID

# 遍历所有bug ID
for bug_id in bug_ids:
    comments_path = os.path.join(base_path, 'bugreport', bug_id, 'comments')
    combined_comments_path = os.path.join(combined_comments_dir, f"{bug_id}_comments_combined.txt")

    # 创建或覆盖已有的合并文件
    with open(combined_comments_path, 'w') as combined_file:
        # 获取评论文件并按照文件名排序
        comment_files = sorted(os.listdir(comments_path))

        # 遍历所有评论文件
        for comment_file in comment_files:
            comment_file_path = os.path.join(comments_path, comment_file)
            if os.path.isfile(comment_file_path):  # 确保是文件
                # 读取评论文件内容并写入合并文件
                with open(comment_file_path, 'r') as file:
                    combined_file.write(file.read() + '\n\n')  # 以空行分隔评论

print("所有评论合并完成，并已存放至 'comments' 目录。")
