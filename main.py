import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()
@dp.message(Command("ip"))
async def get_ip_handler(message: Message) -> None:
    ip = os.popen("upnpc -s | grep ^ExternalIPAddress | cut -c21-").read()[:-1]
    await message.answer(ip)
    await message.answer(html.code(f"ssh arthur@{ip} -t /bin/zsh"))


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
