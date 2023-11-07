import os
import shutil
import csv

def delete_specific_folders(base_dir, ids_file, folder_name):
    # 读取所有的bug id
    with open(ids_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        # 通常CSV的第一行是标题行，如果ids.csv第一行就是数据则下面这行不需要
        # next(csv_reader, None)  # Skip the header
        bug_ids = [row[0] for row in csv_reader]

    # 对于每一个bug id，删除特定的文件夹
    for bug_id in bug_ids:
        specific_folder_path = os.path.join(base_dir, bug_id, folder_name)

        # 检查特定文件夹是否存在
        if os.path.exists(specific_folder_path) and os.path.isdir(specific_folder_path):
            # 删除文件夹
            shutil.rmtree(specific_folder_path)
            print(f"Deleted folder: {specific_folder_path}")
        else:
            print(f"Specific directory for bug ID {bug_id} does not exist or is not a directory.")

    print("Finished processing all bug IDs.")

if __name__ == "__main__":
    base_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
    ids_file = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
    folder_to_delete = 'comment'  # 要删除的文件夹名称
    delete_specific_folders(base_dir, ids_file, folder_to_delete)
