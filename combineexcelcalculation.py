import csv
from datetime import datetime, timedelta

def parse_time(time_str):
    return datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S') if time_str else None

def compute_duration(start, end):
    return end - start if start and end else None

def format_duration(duration):
    return f"{duration.days} days, {duration.seconds // 3600:02}:{duration.seconds % 3600 // 60:02}" if duration else ""

def update_duration_data(csv_file_path):
    new_rows = []
    durations = []
    assigned_durations = []
    wontfix_durations = []
    merged_durations = []
    feedback_durations = []
    last_assigned_durations = []

    with open(csv_file_path, 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            post_time = parse_time(row['Post Time'])
            fixed_time = parse_time(row['Fixed Time'])
            assigned_time = parse_time(row['Assigned Time'])
            wontfix_time = parse_time(row['WontFix Time'])
            merged_time = parse_time(row['Merged Time'])
            feedback_time = parse_time(row['Needs-Feedback Time'])
            last_assigned_time = parse_time(row['Last Assigned Time'])

            duration = compute_duration(post_time, fixed_time)
            assigned_duration = compute_duration(post_time, assigned_time)
            wontfix_duration = compute_duration(post_time, wontfix_time)
            merged_duration = compute_duration(post_time, merged_time)
            feedback_duration = compute_duration(post_time, feedback_time)
            last_assigned_duration = compute_duration(post_time, last_assigned_time)

            if duration: durations.append(duration)
            if assigned_duration: assigned_durations.append(assigned_duration)
            if wontfix_duration: wontfix_durations.append(wontfix_duration)
            if merged_duration: merged_durations.append(merged_duration)
            if feedback_duration: feedback_durations.append(feedback_duration)
            if last_assigned_duration: last_assigned_durations.append(last_assigned_duration)

            row['Duration'] = format_duration(duration)
            row['Duration to Assign'] = format_duration(assigned_duration)
            row['Duration to WontFix'] = format_duration(wontfix_duration)
            row['Duration to Merge'] = format_duration(merged_duration)
            row['Needs-Feedback Time'] = format_duration(feedback_duration)
            row['Last Assigned Duration'] = format_duration(last_assigned_duration)

            new_rows.append(row)

    # Compute averages
    average_duration = sum(durations, timedelta(0)) / len(durations)
    average_assigned_duration = sum(assigned_durations, timedelta(0)) / len(assigned_durations)
    average_wontfix_duration = sum(wontfix_durations, timedelta(0)) / len(wontfix_durations)
    average_merged_duration = sum(merged_durations, timedelta(0)) / len(merged_durations)
    average_feedback_duration = sum(feedback_durations, timedelta(0)) / len(feedback_durations)
    average_last_assigned_duration = sum(last_assigned_durations, timedelta(0)) / len(last_assigned_durations)

    # Write to a new sheet or file
    with open(csv_file_path, 'w', newline='') as file:
        fieldnames = csv_reader.fieldnames + ['Last Assigned Duration']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(new_rows)

    # Return statistics
    return {
        'Average Duration': average_duration,
        'Average Duration to Assign': average_assigned_duration,
        'Average Duration to WontFix': average_wontfix_duration,
        'Average Duration to Merge': average_merged_duration,
        'Average Feedback Duration': average_feedback_duration,
        'Average Last Assigned Duration': average_last_assigned_duration,
        'Counts': {
            'Fixed': len(durations),
            'Assigned': len(assigned_durations),
            'WontFix': len(wontfix_durations),
            'Merged': len(merged_durations),
            'Feedback': len(feedback_durations),
            'Last Assigned': len(last_assigned_durations)
        }
    }

# Example usage
csv_file_path = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/combined_bug_duration.csv'

# 调用函数处理数据并获取统计信息
statistics = update_duration_data(csv_file_path)

# 打印统计结果
print("统计结果：")
for key, value in statistics.items():
    if isinstance(value, dict):
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")
    else:
        print(f"{key}: {value}")