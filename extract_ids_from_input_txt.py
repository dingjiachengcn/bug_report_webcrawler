import re
import csv
import os
import chardet


def extract_ids_from_text(text):
    # 使用正则表达式匹配ID，这里我们假设ID是连续的数字
    return re.findall(r'\b\d{7}\b', text)


def write_ids_to_csv(ids, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID'])  # 写入标题
        for id_ in ids:
            writer.writerow([id_])


def detect_file_encoding(filename):
    with open(filename, 'rb') as f:
        detected = chardet.detect(f.read())
        if detected['confidence'] > 0.9:
            return detected['encoding']
        else:
            return 'ISO-8859-1'



def main():
    # 检测文件编码
    encoding = detect_file_encoding('input.txt')

    # 首先，我们需要读取文本文件的内容
    with open('input.txt', 'r', encoding=encoding) as f:
        content = f.read()

    # 从文本内容中提取ID
    ids = extract_ids_from_text(content)

    # 指定保存到项目文件夹的路径
    project_folder = "/home/jiacheng/bugreport"
    csv_filename = os.path.join(project_folder, 'ids.csv')

    # 将ID写入CSV文件
    write_ids_to_csv(ids, csv_filename)
    print(f"IDs have been written to {csv_filename}")


if __name__ == '__main__':
    main()
