import os


def read_ids_from_csv(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def contains_fuzz_keywords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        if 'fuzz' in content or 'Fuzz' in content:
            return True
    return False

def main():
    ids_path = "/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv"
    bug_report_dir = "/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport/"


    ids = read_ids_from_csv(ids_path)
    for id_ in ids:
        file_path = os.path.join(bug_report_dir, id_, f"{id_}copy.txt")
        if os.path.exists(file_path) and contains_fuzz_keywords(file_path):
            print(id_)


if __name__ == '__main__':
    main()
