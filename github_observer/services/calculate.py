from classes import Github
from typing import List, Tuple
from classes import Member, Repo
from github_api import fetch_repos, fetch_user, fetch_grass_count


async def calculate(members: List[Member], token='') -> Tuple[List[Github], List[Repo]]:
    ret_githubs = []
    ret_repos: List[Repo] = []

    for member in members:
        profile = fetch_user(member.username, token)
        repos = fetch_repos(member.username, token)
        star_count = 0
        for repo in repos:
            ret_repos.append(repo)
        contribution_count = fetch_grass_count(member.username)

        ret_githubs.append(
            Github(
                name=member.name, username=member.username, avatar_url=profile.avatar_url,
                commit_count=contribution_count, star_count=star_count
            )
        )

    return ret_githubs, ret_repos
