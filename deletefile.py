import os


def delete_bugreport_files(parent_folder):
    # 遍历父文件夹下的所有子文件夹
    for subdir in os.listdir(parent_folder):
        subdir_path = os.path.join(parent_folder, subdir)

        # 确保当前路径是一个文件夹
        if os.path.isdir(subdir_path):
            bugreport_file_path = os.path.join(subdir_path, 'bugreport.html')

            # 检查bugreport.html是否存在
            if os.path.exists(bugreport_file_path):
                try:
                    os.remove(bugreport_file_path)
                    print(f"Deleted {bugreport_file_path}")
                except Exception as e:
                    print(f"Failed to delete {bugreport_file_path}. Error: {e}")


if __name__ == '__main__':
    parent_folder_path = "/Users/jiachengding/PycharmProjects/bug_report_webcrawler/bugreport"
    delete_bugreport_files(parent_folder_path)
