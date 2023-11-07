import os
import csv

def delete_specific_files(base_dir, ids_file):
    # 读取所有的bug id
    with open(ids_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        bug_ids = [row[0] for row in csv_reader]

    for bug_id in bug_ids:
        bug_dir = os.path.join(base_dir, bug_id)

        # 检查目录是否存在
        if not os.path.isdir(bug_dir):
            print(f"Bug directory for bug ID {bug_id} does not exist.")
            continue

        # 定义要删除的文件的通配模式
        files_to_delete = [
            f"{bug_id}.txt",
            f"{bug_id}copy.txt"
        ]

        # 遍历目录中的文件
        for file in os.listdir(bug_dir):
            # 构建文件完整路径
            file_path = os.path.join(bug_dir, file)

            # 如果文件符合删除条件且不是'all.txt'，则删除
            if any(file.endswith(pattern) for pattern in files_to_delete) and 'all.txt' not in file:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                else:
                    print(f"File {file_path} does not exist.")

        print(f"Processed bug ID {bug_id}.")

if __name__ == "__main__":
    base_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
    ids_file = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
    delete_specific_files(base_dir, ids_file)
