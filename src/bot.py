import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
SSH_USER = os.getenv("SSH_USER")
SERVER_SHELL = os.getenv("SERVER_SHELL")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


dp = Dispatcher()
@dp.message(Command("ip"))
async def get_ip_handler(message: Message) -> None:
    ip = os.popen("upnpc -s | grep ^ExternalIPAddress | cut -c21-").read()[:-1]
    await message.answer(html.code(f"ssh {SSH_USER}@{ip} -t /bin/{SERVER_SHELL}"))


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
