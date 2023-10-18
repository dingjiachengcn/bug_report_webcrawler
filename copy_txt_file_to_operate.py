import os
import shutil

# 指定bugreport文件夹的路径
bugreport_folder = "/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport"

# 遍历bugreport文件夹下的所有子文件夹
for subdir, dirs, files in os.walk(bugreport_folder):
    for file in files:
        # 检查文件是否为txt文件
        if file.endswith('all.txt'):
            original_file_path = os.path.join(subdir, file)
            # 创建新文件名（加上'copy'后缀）
            new_file_name = file.replace('all.txt', 'copy.txt')
            new_file_path = os.path.join(subdir, new_file_name)

            # 复制文件
            shutil.copy2(original_file_path, new_file_path)

print("复制完成！")