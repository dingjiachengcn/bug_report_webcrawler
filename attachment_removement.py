import os
import shutil
import csv

# 设置源文件夹和目标文件夹
source_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
target_base_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport/attach'
ids_file = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'

# 读取bug ids
with open(ids_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        bug_id = row[0]
        attachment_source_path = os.path.join(source_dir, bug_id, 'attachment')
        attachment_target_path = os.path.join(target_base_dir, bug_id)

        # 确保目标文件夹存在
        if not os.path.exists(attachment_target_path):
            os.makedirs(attachment_target_path)

        # 如果存在源attachment目录
        if os.path.exists(attachment_source_path):
            # 遍历attachment目录中的所有文件和文件夹
            for item in os.listdir(attachment_source_path):
                source_item_path = os.path.join(attachment_source_path, item)
                target_item_path = os.path.join(attachment_target_path, item)

                # 如果是文件夹中的文件，直接移动
                if os.path.isfile(source_item_path):
                    # 如果目标路径已经存在同名文件，则先删除
                    if os.path.exists(target_item_path):
                        os.remove(target_item_path)

                    # 移动文件
                    shutil.move(source_item_path, attachment_target_path)

            # 删除空的源attachment目录
            if not os.listdir(attachment_source_path):
                os.rmdir(attachment_source_path)

            print(f'Moved attachments for bug ID {bug_id}')
        else:
            print(f'No attachment directory found for bug ID {bug_id}')
