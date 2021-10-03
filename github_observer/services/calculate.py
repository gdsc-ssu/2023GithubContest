from classes import Github
from github_api import fetch_repos, fetch_commits


async def calculate(members, token=''):
    githubs = []

    for m in members:
        repos = fetch_repos(m.username, token)
        repoCommit = [len(fetch_commits(r['full_name'], m.username, token))
                      for r in repos]

        # TODO stars 계산도 해야함.
        githubs.append(Github(m.name, m.username, sum(repoCommit), 0))

    return githubs
