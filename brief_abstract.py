import csv
import os
import json
from bs4 import BeautifulSoup

# 设置根目录路径
root_dir = '/home/jiacheng/PycharmProjects/bug_report_webcrawler/bugreport'

def extract_info(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    info = {
        "Starred by": "",
        "Owner": "",
        "CC": [],
        "Status": "",
        "Components": "",
        "Modified": "",
        "Backlog-Rank": "",
        "Editors": "",
        "EstimatedDays": "",
        "NextAction": "",
        "OS": [],
        "Pri": "",
        "Type": "",
        "Labels": []
    }

    # 提取信息
    info["Starred by"] = soup.find(string="Starred by").find_next().get_text(strip=True) if soup.find(
        string="Starred by") else ""
    info["Owner"] = soup.find(string="Owner:").find_next().get_text(strip=True) if soup.find(string="Owner:") else ""
    info["CC"] = [cc.get_text(strip=True) for cc in soup.select("tr.row-cc a[id='user-link']")]
    info["Status"] = soup.find(string="Status:").find_next().get_text(strip=True) if soup.find(string="Status:") else ""
    info["Components"] = soup.find(string="Components:").find_next().get_text(strip=True) if soup.find(
        string="Components:") else ""
    info["Modified"] = soup.find(string="Modified:").find_next().get_text(strip=True) if soup.find(
        string="Modified:") else ""
    info["Backlog-Rank"] = soup.find(string="Backlog-Rank:").find_next().get_text(strip=True) if soup.find(
        string="Backlog-Rank:") else ""
    info["Editors"] = soup.find(string="Editors:").find_next().get_text(strip=True) if soup.find(
        string="Editors:") else ""
    info["EstimatedDays"] = soup.find(string="EstimatedDays:").find_next().get_text(strip=True) if soup.find(
        string="EstimatedDays:") else ""
    info["NextAction"] = soup.find(string="NextAction:").find_next().get_text(strip=True) if soup.find(
        string="NextAction:") else ""
    info["OS"] = [os.get_text(strip=True) for os in soup.select("tr[row-os] a")]
    info["Pri"] = soup.find(string="Pri:").find_next().get_text(strip=True) if soup.find(string="Pri:") else ""
    info["Type"] = soup.find(string="Type:").find_next().get_text(strip=True) if soup.find(string="Type:") else ""
    info["Labels"] = [label.get_text(strip=True) for label in soup.select("div.labels-container a.label")]

    return info

# 读取Bug IDs
with open('/home/jiacheng/PycharmProjects/bug_report_webcrawler/ids.csv', 'r') as ids_file:
    reader = csv.reader(ids_file)
    for row in reader:
        bug_id = row[0]
        file_path = os.path.join(root_dir, f'{bug_id}', f'{bug_id}all.txt')

        # 确保文件存在
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                html_content = file.read()
                bug_info = extract_info(html_content)

                # 保存提取的信息为JSON，文件名为 {bug_id}_brief.json
                json_path = os.path.join(root_dir, f'{bug_id}', f'{bug_id}_brief.json')
                with open(json_path, 'w') as json_file:
                    json.dump(bug_info, json_file, indent=4)

print("Completed extracting and saving bug info as JSON.")
