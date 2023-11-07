import os
import csv

# 设置基础路径和CSV文件路径
base_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler'
ids_csv_path = os.path.join(base_path, 'ids.csv')

# 读取所有bug ID
with open(ids_csv_path, 'r') as file:
    bug_ids = [line.strip() for line in file]

# 遍历所有bug ID
for bug_id in bug_ids:
    comments_path = os.path.join(base_path, 'bugreport', bug_id, 'comments')
    combined_comments_path = os.path.join(comments_path, f"{bug_id}_comments_combined.txt")

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

print("所有评论合并完成。")
