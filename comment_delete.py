import os
import csv

def delete_comment_txt_files(base_dir, ids_file):
    with open(ids_file, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            bug_id = row[0]
            comments_dir = os.path.join(base_dir, bug_id, 'comments')
            if os.path.exists(comments_dir):
                for filename in os.listdir(comments_dir):
                    if filename.endswith('.txt'):
                        file_path = os.path.join(comments_dir, filename)
                        os.remove(file_path)
                        print(f'已删除文件: {file_path}')
            else:
                print(f'评论文件夹 {comments_dir} 不存在。')

# 主程序
def main():
    base_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
    ids_file = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
    delete_comment_txt_files(base_dir, ids_file)

if __name__ == "__main__":
    main()
