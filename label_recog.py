import re
from collections import defaultdict

# 读取文件内容
with open('/home/jiacheng/PycharmProjects/bug_report_webcrawler/labels_cat.txt', 'r') as file:
    content = file.read()

# 这个正则表达式是为了匹配如 -LTS-Merge-Review-96 这类的模式，但不限于此
pattern = re.compile(r"(-[\w]+-[\w]+-[\d]+)")

# 使用defaultdict来存储找到的所有模式
patterns_dict = defaultdict(list)

# 找到所有匹配的模式
matches = pattern.findall(content)
for match in matches:
    # 这里我们将匹配的字符串分为两部分，前缀和数字
    parts = re.match(r"(-[\w]+-[\w]+)-(\d+)", match)
    if parts:
        # 将数字部分作为后缀添加到列表中
        patterns_dict[parts.group(1)].append(parts.group(2))

# 将找到的模式整理为字符串
filtered_content = "\n".join(f"{key}: {' '.join(sorted(set(values)))}" for key, values in patterns_dict.items())

# 写入过滤后的内容到新文件
with open('/home/jiacheng/PycharmProjects/bug_report_webcrawler/labels_cat_filted.txt', 'w') as file:
    file.write(filtered_content)

print("Filtering complete!")
