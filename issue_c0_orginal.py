import os
import re
from html import unescape

# 设置基本路径
base_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport/'

# 读取ids.csv文件中的所有ID
with open('/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv', 'r') as ids_file:
    ids = ids_file.read().splitlines()

for bug_id in ids:
    issue_path = os.path.join(base_path, bug_id, 'issue', f'{bug_id}_c0.txt')
    view_path = os.path.join(base_path, bug_id, 'issue', f'{bug_id}_c0_view.txt')

    # 尝试读取并转换c0.txt文件中的内容
    try:
        with open(issue_path, 'r') as issue_file:
            content = issue_file.read()

            # 移除HTML标签
            content_no_html = re.sub(r'<[^>]+>', '', content)

            # 解码HTML实体
            content_decoded = unescape(content_no_html)

            # 移除JavaScript代码片段
            content_no_js = re.sub(r'<script[^>]*>([\s\S]*?)</script>', '', content_decoded)

            # 保存转换后的内容到新文件中
            with open(view_path, 'w') as view_file:
                view_file.write(content_no_js)

    except FileNotFoundError:
        print(f'文件未找到: {issue_path}')
    except Exception as e:
        print(f'处理文件{issue_path}时出现错误: {e}')
