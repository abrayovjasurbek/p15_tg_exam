from time import sleep
from aiogram.types import FSInputFile
import os
import asyncio
from aiogram.types import Message
from aiogram import Dispatcher, Bot, types
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from main import kunuz

load_dotenv()

url = 'https://kun.uz/'

dp = Dispatcher(storage=MemoryStorage())

TOKEN = os.getenv('token')

@dp.message(CommandStart())
async def startup(message: Message):
    first_name = message.from_user.first_name
    await message.answer(
        f"Hello {first_name}"
    )

@dp.message(lambda msg: msg.text == '/news')
async def enter(message: Message):
    while True:
        await message.answer('Yuklanmoqda ...')
        await kunuz()
        picture = FSInputFile('new.png', filename='screenshot')
        await message.answer_photo(picture)
        sleep(10800)
#         3 soat = 10 800 sekund

async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())