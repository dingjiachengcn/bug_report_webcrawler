import csv

# 文件路径
assigned_csv = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bug_duration (3rd copy).csv'
bug_duration_csv = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bug_duration (6th copy).csv'
output_csv = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/combined_bug_duration.csv'

# 读取assigned时间数据
assigned_data = {}
with open(assigned_csv, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # 跳过标题行
    for row in csv_reader:
        assigned_data[row[0]] = row[1]  # 将Bug ID映射到Last Assigned Time

# 合并数据并写入新文件
with open(bug_duration_csv, 'r', newline='') as infile, open(output_csv, 'w', newline='') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)
    header = next(csv_reader)
    header.append('Last Assigned Time')  # 添加新列标题
    csv_writer.writerow(header)

    for row in csv_reader:
        bug_id = row[0]
        last_assigned_time = assigned_data.get(bug_id, '')
        csv_writer.writerow(row + [last_assigned_time])

print(f"Combined data saved to {output_csv}")
