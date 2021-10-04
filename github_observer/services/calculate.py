from classes import Github
from pprint import pprint
from typing import List
from classes import Member
from github_api import fetch_repos, fetch_user, fetch_grass_count


async def calculate(members: List[Member], token='') -> List[Github]:
    githubs = []

    for member in members:
        profile = fetch_user(member.username, token)
        repos = fetch_repos(member.username, token)
        for repo in repos:
            print(repo.full_name)
        contribution_count = fetch_grass_count(member.username)

        # # TODO stars 계산도 해야함.
        githubs.append(
            Github(name=member.name, username=member.username, avatar_url=profile.avatar_url,
                   commit_count=contribution_count, star_count=0))

        pprint(githubs)
    return githubs
