from .classes import Github
from .githubApi import listsReposForUser, listCommits


async def calculate(members, token=''):
    githubs = []
    #getToken()     # oauth 인증 후 token 받아서 하려고 하다가, github action에서 token 전달
                    # github action token의 경우 시간당 1000개 request 제한임.

    for m in members:
        repos = listsReposForUser(m.username, token)
        repoCommit = [len(listCommits(r['full_name'], token)) for r in repos]

        githubs.append(Github(m.name, m.username, sum(repoCommit), 0))  # TODO stars 계산도 해야함.

    return githubs
