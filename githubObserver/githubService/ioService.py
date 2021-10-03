import csv
import json
from classes import Member


def readMemberList():
    members = []
    with open("./resources/memberList.csv", newline="", encoding='utf-8') as f:
        lines = csv.reader(f, delimiter=",")
        for line in lines:
            try:
                members.append(Member(line[0], line[1], "https://github.com/"+line[1]))
            except Exception as e:
                print(f"error in line : {line}")

    print(members)
    return members


def writeGithubList(githubs):
    dictedGithub = [github.__dict__ for github in githubs]
    githubDict = {"github": dictedGithub}

    with open("./resources/newestGithubs.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(githubDict, ensure_ascii=False))
