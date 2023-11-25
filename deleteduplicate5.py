import os
import re

# 文件夹路径
source_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport_copies'

# 定义要删除的代码片段的正则表达式
patterns_to_remove = [
    re.compile(r"<style>[\s\S]*?</style>", re.MULTILINE),  # 删除<style>...</style>
    re.compile(r"<div>[\s\S]*?</div>", re.MULTILINE),  # 删除所有<div>...</div>
    re.compile(r"\s*<aside>[\s\S]*?</aside>", re.MULTILINE),  # 删除所有<aside>...</aside>
    re.compile(r"<!---->.*?<strong><!---->Labels:</strong>", re.MULTILINE),  # 删除特定的标记，但保留Labels:
    # 添加其他需要删除的代码段的正则表达式
]

# 空行的正则表达式
empty_line_pattern = re.compile(r"^\s*$", re.MULTILINE)

# 遍历目标目录中的所有文件
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)

    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 删除指定的代码片段
        for pattern in patterns_to_remove:
            content = pattern.sub('', content)

        # 删除所有空行
        content = empty_line_pattern.sub('', content)

        # 将修改后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

print("Completed removing additional code snippets and empty lines from all.txt files.")
