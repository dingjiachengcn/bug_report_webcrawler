import os

# 定义bugreport的目录路径
bugreport_folder = "/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport"

# 列出所有bugreport目录下的子文件夹
subdirs = [os.path.join(bugreport_folder, d) for d in os.listdir(bugreport_folder) if os.path.isdir(os.path.join(bugreport_folder, d))]

# 在每个子文件夹中创建一个名为'attachment'的子文件夹
for subdir in subdirs:
    comment_path = os.path.join(subdir, 'comment')
    if not os.path.exists(comment_path):
        os.makedirs(comment_path)
        print(f"Created 'comment' folder in {subdir}")
    else:
        print(f"'comment' folder already exists in {subdir}")
