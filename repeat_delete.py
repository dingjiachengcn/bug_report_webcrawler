import hashlib
import os
import csv


def calculate_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()


def remove_duplicate_files(base_dir, ids_file):
    with open(ids_file, 'r') as ids:
        reader = csv.reader(ids)
        for row in reader:
            bug_id = row[0]
            comments_dir = os.path.join(base_dir, bug_id, 'comments')
            if not os.path.exists(comments_dir):
                continue

            seen_hashes = {}
            for filename in os.listdir(comments_dir):
                filepath = os.path.join(comments_dir, filename)
                file_hash = calculate_file_hash(filepath)

                if file_hash in seen_hashes:
                    os.remove(filepath)
                    print(f"Removed duplicate file: {filepath}")
                else:
                    seen_hashes[file_hash] = filepath


if __name__ == "__main__":
    base_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'
    ids_file = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv'
    remove_duplicate_files(base_dir, ids_file)
