import requests
# from pprint import pprint
from typing import List
from classes import Profile, Repo, Owner

"""
oauth를 이용해 token을 얻는 방법. 사전에 GET https://github.com/login/oauth/authorize 으로 callback code를 얻어야함.
def getToken():
    query_url = f"https://github.com/login/oauth/access_token"
    datas = {
        "client_id": {clientId},
        "client_secret": {clientSecret},
        "code": {code}
    }
    headers = {
        'accept': 'application/vnd.github.v3+json'
    }
    r = requests.post(query_url, data=datas, headers=headers)
    return r.json()
"""


def fetch_user(username: str, token: str) -> Profile:
    query_url = f"https://api.github.com/users/{username}"
    headers = {
        'accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {token}'
    }
    r = requests.get(query_url, headers=headers)
    return Profile(r.json()['avatar_url'])


def fetch_repos(username: str, token: str) -> List[Repo]:
    """
    https://docs.github.com/en/rest/reference/repos#list-repositories-for-a-user
    """
    query_url = f"https://api.github.com/users/{username}/repos"
    params = {
        "state": "open",
    }
    headers = {
        'accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {token}'
    }
    response = requests.get(query_url, headers=headers, params=params)
    repos = [
        Repo(
            created_at=repo['created_at'],
            description=repo['description'],
            language=repo['language'],
            name=repo['name'],
            full_name=repo['full_name'],
            owner=Owner(
                avatar_url=repo['owner']['avatar_url'],
                login=repo['owner']['login'],
                type=repo['owner']['type']
            ),
            private=repo['private'],
            stargazers_count=repo['stargazers_count'],
        ) for repo in response.json()
    ]
    return repos


def fetch_commits(full_name: str, author: str, token: str):
    """
    https://docs.github.com/en/rest/reference/repos#list-commits
    """
    query_url = f"https://api.github.com/repos/{full_name}/commits"
    params = {
        "since": "2019-10-02T00:00:00+0900",
        "until": "2021-11-07T00:00:00+0900",
        "author": {author}
    }
    headers = {
        'accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {token}'
    }
    r = requests.get(query_url, headers=headers, params=params)
    return r.json()
