class Member:
    def __init__(self, name, username, github_url):
        self.name = name
        self.username = username
        self.github_url = github_url

    def __repr__(self):
        return f"[Member] name: {self.name}, username: {self.username}, github_url: {self.github_url}"


class Github:
    def __init__(self, name, username, commit_count, star_count):
        self.name = name
        self.username = username
        self.commit_count = commit_count
        self.star_count = star_count

    def __repr__(self):
        return f"[Github] name: {self.name}, username: {self.username}, commit_count: {self.commit_count}, star_count: {self.star_count}"
