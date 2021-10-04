import requests
from datetime import datetime
from typing import List
from classes import Profile, Repo, User, Commit
from bs4 import BeautifulSoup

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
        "sort": "pushed",
        "type": "all",
        "per_page": 100,
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
            owner=User(
                avatar_url=repo['owner']['avatar_url'],
                login=repo['owner']['login'],
                type=repo['owner']['type']
            ),
            private=repo['private'],
            stargazers_count=repo['stargazers_count'],
        ) for repo in response.json()
    ]
    return repos


def fetch_commits(full_name: str, author: str, token: str) -> List[Commit]:
    """
    https://docs.github.com/en/rest/reference/repos#list-commits

    :param full_name: 'repo/user'
    :param author: GitHub login or email address by which to filter by commit author
    """
    query_url = f"https://api.github.com/repos/{full_name}/commits"
    params = {
        "since": "2021-10-02T00:00:00Z",
        "until": "2021-11-07T00:00:00Z",
        "author": {author},
    }
    headers = {
        "accept": "application/vnd.github.v3+json",
        "Authorization": f"token {token}",
    }
    r = requests.get(query_url, headers=headers, params=params)
    ret = [Commit(
        url=body['commit']['url'],
        author=body['commit']['author'],
        comment_count=body['commit']['comment_count'],
        committer=body['commit']['committer'],
        message=body['commit']['message'],
        tree=body['commit']['tree'],
        verification=body['commit']['verification']
    ) for body in r.json()]

    return ret


def fetch_grass_count(login: str, since: str = '2021-10-02', until: str = '2021-11-07') -> int:
    r = requests.get('https://github.com/{}'.format(login))
    soup = BeautifulSoup(r.text, 'html.parser')
    days = soup.find_all(class_='ContributionCalendar-day')
    since_date = datetime.strptime(since, '%Y-%m-%d')
    until_date = datetime.strptime(until, '%Y-%m-%d')
    ret = 0

    for day in days:
        data_date = day.get('data-date')
        data_count = day.get('data-count')

        if not data_date or not data_count:
            continue
        contribution_date = datetime.strptime(data_date, '%Y-%m-%d')

        if since_date <= contribution_date <= until_date:
            ret += int(data_count)

    return ret
