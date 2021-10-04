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
class Owner:
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
    owner: Owner
    private: bool
    stargazers_count: int
