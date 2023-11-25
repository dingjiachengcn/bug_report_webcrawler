import os

# 文件夹路径
source_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport_copies'

# 遍历目标目录中的所有文件
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)

    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 分割文件内容为段落
        paragraphs = content.split('\n\n')  # 假设两个换行符作为段落分隔符

        # 使用集合去除重复段落
        unique_paragraphs = set(paragraphs)

        # 将去重后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            for paragraph in unique_paragraphs:
                file.write(paragraph + '\n\n')  # 在每个段落后添加两个换行符

print("Completed removing duplicates from all.txt files.")
