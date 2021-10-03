from classes import Github
from pprint import pprint
from typing import List
from classes import Member
from github_api import fetch_repos, fetch_commits, fetch_user


async def calculate(members: List[Member], token='') -> List[Github]:
    githubs = []

    for m in members:
        profile = fetch_user(m.username, token)
        print(profile.avatar_url)
        repos = fetch_repos(m.username, token)
        repoCommit = [len(fetch_commits(r['full_name'], m.username, token))
                      for r in repos]

        # # TODO stars 계산도 해야함.
        githubs.append(
            Github(name=m.name, username=m.username, avatar_url=profile.avatar_url,
                   commit_count=sum(repoCommit), star_count=0))

        pprint(githubs)
    return githubs
