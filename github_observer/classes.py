import dataclasses


@dataclasses.dataclass(unsafe_hash=True)
class Member:
    name: str
    username: str
    github_url: str


@dataclasses.dataclass(unsafe_hash=True)
class Github:
    name: str
    username: str
    avatar_url: str
    commit_count: int
    star_count: int


@dataclasses.dataclass(unsafe_hash=True)
class Profile:
    avatar_url: str
