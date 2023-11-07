import os
import csv

# 设置bug报告的根目录和CSV文件的路径
bug_report_root = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
ids_csv_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'

# 读取CSV文件中的所有bug ID
with open(ids_csv_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    bug_ids = [row[0] for row in reader]  # 假设ID是CSV的第一列

# 遍历所有bug ID
for bug_id in bug_ids:
    # 设置评论文件的目录路径
    comments_dir = os.path.join(bug_report_root, bug_id, 'comments')
    # 获取该目录下所有文件
    file_paths = [os.path.join(comments_dir, filename) for filename in os.listdir(comments_dir)]
    # 对文件路径进行排序以确保顺序（这可能需要根据实际文件名格式调整）
    file_paths.sort(key=lambda x: int(x.split('_comment_')[-1].split('.txt')[0]))

    # 重新编号文件
    for i, file_path in enumerate(file_paths, start=1):
        new_file_name = f"{bug_id}_comment_{i}.txt"
        new_file_path = os.path.join(comments_dir, new_file_name)
        os.rename(file_path, new_file_path)

print("重命名完成。")
