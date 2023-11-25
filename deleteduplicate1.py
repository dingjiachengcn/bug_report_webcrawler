import os
import re

# 文件夹路径
source_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport_copies'

# 定义要删除的代码片段的正则表达式
patterns_to_remove = [
    re.compile(
        r"\s*// Google Analytics[\s\S]*?\(window,document,'script','//www\.google-analytics\.com/analytics\.js','ga'\);\)\(\);<\/script>",
        re.MULTILINE),
    re.compile(r"\s*:host \{[\s\S]*?box-sizing: border-box;\s*font-size: var\(--chops-main-font-size\);\s*\}",
               re.MULTILINE)
]

# 遍历目标目录中的所有文件
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)

    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 删除指定的代码片段
        for pattern in patterns_to_remove:
            content = pattern.sub('', content)

        # 将修改后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

print("Completed removing specific code snippets from all.txt files.")
