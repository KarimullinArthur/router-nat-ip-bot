#!/usr/bin/env python
import asyncio
import re
import os

import aiohttp
from dotenv import load_dotenv


load_dotenv()
CHANNEL_URL = os.getenv("CHANNEL_URL")


async def get_ip(channel_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(channel_url) as resp:
            rsp = await resp.text()
            ip = re.findall(r"[0-9]+(?:\.[0-9]+){3}", rsp)
            return ip[0]


async def main():
    print(await get_ip(CHANNEL_URL))


if __name__ == "__main__":
    asyncio.run(main())
