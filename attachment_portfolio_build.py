import os

# 定义bugreport的目录路径
bugreport_folder = "/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport"

# 列出所有bugreport目录下的子文件夹
subdirs = [os.path.join(bugreport_folder, d) for d in os.listdir(bugreport_folder) if os.path.isdir(os.path.join(bugreport_folder, d))]

# 在每个子文件夹中创建一个名为'attachment'的子文件夹
for subdir in subdirs:
    attachment_path = os.path.join(subdir, 'attachment')
    if not os.path.exists(attachment_path):
        os.makedirs(attachment_path)
        print(f"Created 'attachment' folder in {subdir}")
    else:
        print(f"'attachment' folder already exists in {subdir}")
