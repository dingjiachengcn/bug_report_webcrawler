import os
import requests

def fetch_and_save_content(bug_id):
    # 基于提供的bug_id构建URL
    url = f"https://bugs.chromium.org/p/chromium/issues/detail?id={bug_id}"

    response = requests.get(url)
    response.raise_for_status()

    # 定义桌面上的主目录和子目录路径
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    main_directory = os.path.join(desktop, 'bug')
    sub_directory = os.path.join(main_directory, str(bug_id))

    # 如果主目录和子目录不存在，则创建
    if not os.path.exists(main_directory):
        os.makedirs(main_directory)
    if not os.path.exists(sub_directory):
        os.makedirs(sub_directory)

    # 在子目录内保存.txt文件
    file_path = os.path.join(sub_directory, f"{bug_id}.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(response.text)

    print(f"Saved source code for bug ID {bug_id} to: {file_path}")

if __name__ == "__main__":
    bug_id = 1485783
    bug_id = 1482849
    fetch_and_save_content(bug_id)
