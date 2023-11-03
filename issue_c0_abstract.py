import os
import csv
import re

# 设置基本路径
base_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport/'

# 正则表达式匹配开始标记
start_pattern = re.compile(r'<!---->\s*</select>\s*</div>', re.DOTALL)

# 正则表达式匹配结束标记
end_pattern = re.compile(r'</span><mr-comment-content></mr-comment-content>', re.DOTALL)

# 读取ids.csv文件中的所有ID
with open('/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv', 'r') as ids_file:
    csv_reader = csv.reader(ids_file)
    for row in csv_reader:
        bug_id = row[0].strip()  # 移除可能的空格
        copy_path = os.path.join(base_path, bug_id, f'{bug_id}copy.txt')
        issue_path = os.path.join(base_path, bug_id, 'issue', f'{bug_id}_c0.txt')

        # 确保issue文件夹存在
        os.makedirs(os.path.dirname(issue_path), exist_ok=True)

        # 尝试读取并提取copy.txt文件中的内容
        try:
            with open(copy_path, 'r') as copy_file:
                content = copy_file.read()

                # 查找所有匹配开始标记的位置
                starts = [match for match in start_pattern.finditer(content)]

                # 从第一个开始标记之后查找第一个结束标记的位置
                if starts:
                    first_start = starts[0]
                    content_after_first_start = content[first_start.end():]
                    end_match = end_pattern.search(content_after_first_start)

                    if end_match:
                        # 提取开头和第一个结束标记之间的内容
                        issue_content = content_after_first_start[:end_match.start()].strip()

                        # 将提取出的内容保存到新文件中
                        with open(issue_path, 'w') as issue_file:
                            issue_file.write(issue_content)
                    else:
                        print(f'结束标签未找到：{bug_id}')
                else:
                    print(f'开始标签未找到：{bug_id}')

        except FileNotFoundError:
            print(f'文件未找到: {copy_path}')
        except Exception as e:
            print(f'处理文件{copy_path}时出现错误: {e}')
