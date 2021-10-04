import csv
from dataclasses import asdict
import json
from typing import List
from classes import Member, Github


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


def write_githubs(githubs: List[Github]):
    githubs = [asdict(github) for github in githubs]
    github_dict = {"github": githubs}

    with open("./resources/githubs.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(github_dict, ensure_ascii=False, indent=2))


def write_markdown(githubs: List[Github]):
    markdown = ""
    template = """
<h2 align="center">천하제일 깃허브 자랑대회 리더보드</h2>

<table align="center">
  <thead>
    <tr>
      <th>
        등수
      </th>
      <th>
        유저프로필
      </th>
      <th>
        닉네임
      </th>
      <th>
        누적커밋수 (2021.10.2~)
      </th>
    </tr>
  </thead>
  <tbody>
{rows}
  </tbody>
</table>
    """

    sorted_githubs = sorted(
        githubs, key=lambda github: github.commit_count, reverse=True)
    rows = [
        """    <tr>
      <td align="center">
        {rank}등
      </td>
      <td align="center">
        <a href="{github_url}" >
          <img width="56" alt="image" src="{avatar_url}">
        </a>
      </td>
      <td align="center">
      <a href="{github_url}" >
          {username}
      </a>
      </td>
      <td align="center">
        {commit_count}
      </td>
    </tr>""".format(
            rank=rank + 1,
            username=github.username,
            github_url=f"https://github.com/{github.username}", avatar_url=github.avatar_url,
            commit_count=github.commit_count)
        for rank, github in enumerate(sorted_githubs)
    ]
    markdown = template.format(rows='\n'.join(rows))

    with open("./resources/output/profile/README.md", "w", encoding="utf-8") as f:
        f.write(markdown)
