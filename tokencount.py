import csv
import os

def count_tokens(text):
    # 简单的token计算方式，根据空格分割
    return len(text.split())

def main():
    base_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler'
    ids_file = os.path.join(base_dir, 'ids.csv')
    output_csv = os.path.join(base_dir, 'token_count.csv')

    total_tokens = 0
    bug_count = 0
    token_counts = []

    with open(ids_file, mode='r', encoding='utf-8') as ids_csv:
        reader = csv.reader(ids_csv)
        next(reader)  # 跳过标题行

        for row in reader:
            bug_id = row[0]
            issue_file = os.path.join(base_dir, 'issue', f'{bug_id}_c0_view.txt')

            if os.path.exists(issue_file):
                with open(issue_file, 'r', encoding='utf-8') as file:
                    content = file.read()
                    token_count = count_tokens(content)
                    token_counts.append((bug_id, token_count))
                    total_tokens += token_count
                    bug_count += 1

    # 计算平均token数
    average_tokens = total_tokens / bug_count if bug_count > 0 else 0

    # 将结果写入到新的CSV文件
    with open(output_csv, 'w', newline='', encoding='utf-8') as out_csv:
        writer = csv.writer(out_csv)
        writer.writerow(['Bug ID', 'Token Count'])
        writer.writerows(token_counts)
        writer.writerow(['Average', average_tokens])
        writer.writerow(['Total', total_tokens])

    print(f"Token counts saved to {output_csv}")

if __name__ == "__main__":
    main()
