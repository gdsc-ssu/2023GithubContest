import csv
import json
from typing import List
from classes import Member


def read_members() -> List[Member]:
    members = []
    with open("./resources/member_list.csv", newline="", encoding='utf-8') as f:
        lines = csv.reader(f, delimiter=",")
        for line in lines:
            try:
                members.append(
                    Member(name=line[0], username=line[1], github_url="https://github.com/" + line[1]))
            except Exception as e:
                print(f"error in line : {line}")

    return members


def write_githubs(githubs):
    dicted_github = [github.__dict__ for github in githubs]
    github_dict = {"github": dicted_github}

    with open("./resources/githubs.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(github_dict, ensure_ascii=False, indent=2))
