
# 2021 GDSC Soongsil Github Contest

## About The Project

#### :crown:천하제일 깃허브 자랑대회:crown:

<img width="700" alt="image" src="https://user-images.githubusercontent.com/64878866/135946981-91e8c9e0-ab8c-4bc6-b595-6b3471a9ec4d.png">

2021.10.02 ~ 2021.11.06 동안 GDSC Soongsil 멤버 대상으로 `천하제일 깃허브 자랑대회` 이벤트가 진행됩니다.

이 프로젝트는 참여 멤버들의 contribution 현황과 star 개수를 자동으로 수집하고, [그룹 profile의 리더보드](https://github.com/gdsc-ssu/.github/tree/main/profile)에 update 하기 위해 시작하였습니다.

<img width="700" alt="image" src="https://user-images.githubusercontent.com/13645032/135944941-fd0f8504-f39f-4e13-83ef-56a9991b6fba.png">

### Built With

- Python

- Github Action

- Crawling & Github Api

   [Github Api](https://docs.github.com/en/rest) 사용을 전제로 합니다.
   (Github Api로 repo를 가져올 때 최신 그룹의 repo는 제외되는 이슈가 있어, `contribution count` 체크의 경우 개인 profile 페이지에서 crawling 하는 방법으로 변경하였습니다.)

## Getting Started

### Preparation

1. **member list**

   참가자들의 명단은 [CSV파일](./github_observer/resources/member_list.csv) 에서 관리됩니다.

   참가자를 등록하는 경우 이미 작성된 데이터를 참고하여 `이름,깃헙username` 형식으로 추가해주세요.

2. **github token**

   Github API 및 Github Action 사용을 위해 토큰 발급이 필요합니다.

   https://github.com/settings/tokens 에서 generate new token 을 통해서 새로운 토큰을 발급받으세요.

   repo, user, workflow 권한을 필요로 합니다.

   [Action Workflow](./github/workflows/updateGithubCommitAndStars.yml)에서의 사용을 위해 Repository secrets에 등록해주세요.

   <img width="550" alt="image" src="https://user-images.githubusercontent.com/64878866/135950383-11f3ed65-74f4-46f9-ad6c-1423e2ad5b08.png">

   ```yml
   - name: Run
     run: python main.py ${{ secrets.GHB_PAT }}
     working-directory: 'github_observer'
   ```
   
   Github API rate limit 참고 : https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting

### Installation

```
git clone https://github.com/gdsc-ssu/2021GithubContest.git

python ./github_observer/main.sh {github_token}
```

### Usage

1. **modify destination path**

   [Action Workflow](./github/workflows/updateGithubCommitAndStars.yml)에서 destination-github-username, destination-repository-name을 업데이트할 레포지토리 정보로 변경해주세요.

2. **change cron schedule**

   현재 12시간 간격(0시, 12시)으로 github action을 통해서 테이블을 update하고 [gdsc-ssu/.github](https://github.com/gdsc-ssu/.github)에 push합니다.
   
   수정을 원하신다면 [Action Workflow](./github/workflows/updateGithubCommitAndStars.yml)에서 `cron schedule expressions`을 수정해주세요.

