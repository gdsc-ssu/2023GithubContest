import asyncio
import sys
from githubService import calculateService, ioService


async def main(token):
    members = ioService.readMemberList()
    githubs = await calculateService.calculate(members, token)
    ioService.writeGithubList(githubs)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(sys.argv[1]))
    loop.close()
