import os
import requests

def fetch_and_save_content(bug_id):
    # construct url by using bug id
    url = f"https://bugs.chromium.org/p/chromium/issues/detail?id={bug_id}"

    response = requests.get(url)
    response.raise_for_status()

    # define the main cate and sub cate route on desktop
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    main_directory = os.path.join(desktop, 'bug')
    sub_directory = os.path.join(main_directory, str(bug_id))

    # if main cate and sub cate not exist, then create it
    if not os.path.exists(main_directory):
        os.makedirs(main_directory)
    if not os.path.exists(sub_directory):
        os.makedirs(sub_directory)

    # save .txt on sub cate
    file_path = os.path.join(sub_directory, f"{bug_id}.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(response.text)

    print(f"Saved source code for bug ID {bug_id} to: {file_path}")

if __name__ == "__main__":
    bug_id = 1485783
    bug_id = 1482849
    fetch_and_save_content(bug_id)
