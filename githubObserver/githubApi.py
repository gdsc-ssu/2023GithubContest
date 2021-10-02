import requests

# oauth를 이용해 token을 얻는 방법. 사전에 GET https://github.com/login/oauth/authorize 으로 callback code를 얻어야함.
# def getToken():
    # query_url = f"https://github.com/login/oauth/access_token"
    # datas = {
    #     "client_id": {clientId},
    #     "client_secret": {clientSecret},
    #     "code": {code}
    # }
    # headers = {
    #     'accept': 'application/vnd.github.v3+json'
    # }
    # r = requests.post(query_url, data=datas, headers=headers)
    #
    # return r.json()


# https://docs.github.com/en/rest/reference/repos#list-repositories-for-a-user
def listsReposForUser(username, token=''):
    query_url = f"https://api.github.com/users/{username}/repos"
    params = {
        "state": "open",
    }
    headers = {
        'accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {token}'
    }
    r = requests.get(query_url, headers=headers, params=params)

    return r.json()


# https://docs.github.com/en/rest/reference/repos#list-commits
def listCommits(fullname, commitAuthor, token=''):
    query_url = f"https://api.github.com/repos/{fullname}/commits"
    params = {
        "since": "2019-10-02T00:00:00+0900",
        "until": "2021-11-07T00:00:00+0900",
        "author": {commitAuthor}
    }
    headers = {
        'accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {token}'
    }
    r = requests.get(query_url, headers=headers, params=params)
    return r.json()
