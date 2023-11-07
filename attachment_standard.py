import os
import shutil
import csv

def move_files_up(base_dir, ids_file):
    # 读取所有的bug id
    with open(ids_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        bug_ids = [row[0] for row in csv_reader]

    for bug_id in bug_ids:
        attachment_dir = os.path.join(base_dir, bug_id, 'attachment')

        # 检查attachment目录是否存在
        if os.path.isdir(attachment_dir):
            # 将文件移动到上一级目录
            for filename in os.listdir(attachment_dir):
                old_file = os.path.join(attachment_dir, filename)
                new_file = os.path.join(base_dir, bug_id, filename)

                # 防止覆盖现有文件，确保目标路径中文件不存在
                if not os.path.exists(new_file):
                    shutil.move(old_file, new_file)
                    print(f"Moved file to: {new_file}")
                else:
                    print(f"File already exists, not moved: {new_file}")

            # 尝试删除空的attachment目录
            try:
                os.rmdir(attachment_dir)
                print(f"Removed empty directory: {attachment_dir}")
            except OSError as e:
                print(f"Directory not empty or other error: {e}")

        else:
            print(f"Attachment directory does not exist for bug ID {bug_id}: {attachment_dir}")

        print(f"Processed bug ID {bug_id}.")

if __name__ == "__main__":
    base_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport/attach'
    ids_file = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
    move_files_up(base_dir, ids_file)
