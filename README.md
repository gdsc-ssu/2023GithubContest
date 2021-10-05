
# `github-contest`

참가자들의 명단을 [CSV파일](./github_observer/resources/member_list.csv) 에서 읽어서 다음과같은 랭킹 테이블을 생성합니다.

<img width="1308" alt="image" src="https://user-images.githubusercontent.com/13645032/135944941-fd0f8504-f39f-4e13-83ef-56a9991b6fba.png">

매일 0시, 12시마다 github action을 통해서 테이블을 업데이트하고 [gdsc-ssu/.github](https://github.com/gdsc-ssu/.github) 에 푸쉬합니다.

## 준비물

github API를 사용하기 위해서 토큰발급이 필요합니다.

[액션 워크플로우 yml 파일](./github/workflows/updateGithubCommitAndStars.yml)에서 A_GITHUB_TOKEN 으로 사용됩니다.

```yml
      - name: Run
        run: python main.py ${{ secrets.A_GITHUB_TOKEN }}
        working-directory: 'github_observer'
```

### 토큰 발급받기

https://github.com/settings/tokens 에서 generate new token 을 통해서 새로운 토큰을 발급받으세요.

<img width="1013" alt="image" src="https://user-images.githubusercontent.com/13645032/135945311-9dbbbf19-e39b-4de8-8e17-1646f81cd3d1.png">

repo, user, workflow(?) 권한을 필요로합니다.

https://github.com/{user_name}/{repo_name}/settings/secrets/actions 에서 Repository secrets 를 생성해줍니다.

<img width="1262" alt="image" src="https://user-images.githubusercontent.com/13645032/135945515-05d6bdd4-5b31-4104-bcef-a023fa13736d.png">

## 커스터마이징 하기

[액션 워크플로우 yml 파일](./github/workflows/updateGithubCommitAndStars.yml)에서 destination-github-username, destination-repository-name을 업데이트할 레포지토리 정보로 변경해줍니다.

