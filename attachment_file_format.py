import os


def extract_file_extensions(directory):
    """遍历指定的目录的子目录中的attachment目录，收集并返回所有唯一的文件扩展名"""
    unique_extensions = set()

    for subdir in os.listdir(directory):
        attachment_dir = os.path.join(directory, subdir, 'attachment')
        if os.path.isdir(attachment_dir):
            for filename in os.listdir(attachment_dir):
                _, extension = os.path.splitext(filename)
                unique_extensions.add(extension)

    return unique_extensions


def main():
    base_path = "/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport"
    extensions = extract_file_extensions(base_path)

    print("在指定的目录的子目录中的attachment目录中找到的所有唯一文件扩展名：")
    for ext in sorted(extensions):
        print(ext)


if __name__ == '__main__':
    main()
