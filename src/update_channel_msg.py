#!/usr/bin/env python

import asyncio
from datetime import datetime
import os

from aiogram import Bot
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
MESSAGE_ID = os.getenv("MESSAGE_ID")


async def update_message():
    async with Bot(token=TOKEN) as bot:
        ip = os.popen("upnpc -s | grep ^ExternalIPAddress | cut -c21-").read()[:-1]
        if ip == "":
            exit(1)
        msg = f"""📅 {datetime.strftime(datetime.now(), format="%Y-%m-%d %H:%M:%S")}
📡 {ip}
    """
        await bot.edit_message_text(text=msg, chat_id=CHANNEL_ID, message_id=MESSAGE_ID)


async def main():
    await update_message()


if __name__ == "__main__":
    asyncio.run(main())
