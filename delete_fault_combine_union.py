import os
import csv


def remove_specific_files(base_dir, ids_file, keywords):
    with open(ids_file, 'r') as ids:
        reader = csv.reader(ids)
        for row in reader:
            bug_id = row[0]
            comments_dir = os.path.join(base_dir, bug_id, 'comments')
            if not os.path.exists(comments_dir):
                continue

            for filename in os.listdir(comments_dir):
                if any(keyword in filename for keyword in keywords):
                    filepath = os.path.join(comments_dir, filename)
                    os.remove(filepath)
                    print(f"Deleted: {filepath}")


if __name__ == "__main__":
    base_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
    ids_file = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
    keywords = ['combine', 'union']
    remove_specific_files(base_dir, ids_file, keywords)
