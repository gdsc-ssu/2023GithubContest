class Member:
    def __init__(self, name, username, githubUrl):
        self.name = name
        self.username = username
        self.githubUrl = githubUrl

    def __str__(self):
        return f"[Member] name: {self.name}, username: {self.username}, githubUrl: {self.githubUrl}"


class Github:
    def __init__(self, name, username, commitCount, starCount):
        self.name = name
        self.username = username
        self.commitCount = commitCount
        self.starCount = starCount

    def __str__(self):
        return f"[Github] name: {self.name}, username: {self.username}, commitCount: {self.commitCount}, starCount: {self.starCount}"
