import csv
from dataclasses import asdict
import json
from typing import List
from classes import Member, Github, Repo


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


def write_markdown(githubs: List[Github], repos: List[Repo]):
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
{github_rows}
  </tbody>
</table>

<h2 align="center">인기 레포지토리 (2021.10.2~)</h2>

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
        레포지토리
      </th>
      <th>
        stargazers
      </th>
    </tr>
  </thead>
  <tbody>
{repo_rows}
  </tbody>
</table>
    """

    sorted_githubs = sorted(
        githubs, key=lambda github: github.commit_count, reverse=True)
    sorted_repos = sorted(
        repos, key=lambda repo: repo.stargazers_count, reverse=True
    )
    github_rows = [
        """    <tr>
      <td align="center">
        {rank}등
      </td>
      <td align="center">
        <a href="{github_url}" >
          <img width="40" alt="image" src="{avatar_url}">
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
    repo_rows = [
        """    <tr>
      <td align="center">
        {rank}등
      </td>
      <td align="center">
        <a href="{github_url}" >
          <img width="40" alt="image" src="{avatar_url}">
        </a>
      </td>
      <td align="center">
        <a href="{repo_url}" >
          {full_name}
        </a>
      </td>
      </td>
      <td align="center">
        {stargazers_count}
      </td>
    </tr>""".format(
            rank=rank + 1,
            full_name=repo.full_name,
            repo_url=f"https://github.com/{repo.full_name}",
            stargazers_count=repo.stargazers_count,
            github_url=f"https://github.com/{repo.owner.login}",
            avatar_url=repo.owner.avatar_url,
        )
        for rank, repo in enumerate(sorted_repos)
    ]
    markdown = template.format(
        github_rows='\n'.join(github_rows[:6]),
        repo_rows='\n'.join(repo_rows[:6])
    )

    with open("./resources/output/profile/README.md", "w", encoding="utf-8") as f:
        f.write(markdown)
