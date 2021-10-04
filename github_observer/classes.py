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


@dataclasses.dataclass
class User:
    avatar_url: str
    login: str
    type: str


@dataclasses.dataclass(unsafe_hash=True)
class Repo:
    created_at: str  # '2016-12-28T03:58:29Z',
    name: str  # 'jelly-translator',
    full_name: str  # 'gomjellie/jelly-translator'
    description: str
    language: str
    owner: User
    private: bool
    stargazers_count: int


@dataclasses.dataclass(unsafe_hash=True)
class Author:
    name: str
    email: str
    date: str


@dataclasses.dataclass(unsafe_hash=True)
class Commiter:
    name: str
    email: str
    date: str


@dataclasses.dataclass(unsafe_hash=True)
class Commit:
    url: str
    author: Author
    committer: Commiter
    message: str
    tree: any
    comment_count: int
    verification: any


@dataclasses.dataclass(unsafe_hash=True)
class CommitWrapper:
    author: User
    comments_url: str
    commit: Commit
    commiter: User
