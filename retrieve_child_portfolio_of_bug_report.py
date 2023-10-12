import csv
import os

# CSV文件的路径
csv_file_path = 'ids.csv'
# 主文件夹的路径
bugreport_folder = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'

def create_bug_folders(csv_path, main_folder):
    with open(csv_path, 'r') as csvfile:
        # 使用CSV reader读取文件内容
        csvreader = csv.reader(csvfile)
        # 跳过CSV的标题（如果有的话）
        next(csvreader, None)

        # 遍历每个bug ID
        for row in csvreader:
            bug_id = row[0]
            # 创建bug ID对应的文件夹路径
            folder_path = os.path.join(main_folder, bug_id)
            # 检查文件夹是否已存在，如果不存在则创建
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Folder created for bug ID: {bug_id}")
            else:
                print(f"Folder already exists for bug ID: {bug_id}")

if __name__ == '__main__':
    create_bug_folders(csv_file_path, bugreport_folder)