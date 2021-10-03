import asyncio
import sys
from services import calculate, io


async def main(token):
    members = io.read_members()
    githubs = await calculate.calculate(members, token)
    io.write_githubs(githubs)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(sys.argv[1]))
    loop.close()
