import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold, italic

API_TOKEN = '6137850721:AAFSamidQjOex0cjEF5G1SYqtj1knbeZHz8'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

resume_data = []

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привет! Я помогу тебе собрать данные для резюме. Пожалуйста, введите ваше имя:")

@dp.message_handler(lambda message: len(resume_data) == 0)
async def process_name(message: types.Message):
    name = message.text
    resume_data.append(name)
    await message.reply("Введите вашу фамилию:")

@dp.message_handler(lambda message: len(resume_data) == 1)
async def process_surname(message: types.Message):
    surname = message.text
    resume_data.append(surname)
    await message.reply("Введите ваш возраст:")

@dp.message_handler(lambda message: len(resume_data) == 2)
async def process_age(message: types.Message):
    age = message.text
    resume_data.append(age)
    await message.reply("Введите вашу почту:")

@dp.message_handler(lambda message: len(resume_data) == 3)
async def process_email(message: types.Message):
    email = message.text
    resume_data.append(email)

    resume_text = text(
        "Ваше резюме:\n\n",
        bold("Имя:"), resume_data[0], "\n",
        bold("Фамилия:"), resume_data[1], "\n",
        bold("Возраст:"), resume_data[2], "\n",
        bold("Почта:"), resume_data[3], "\n"
    )

    await message.reply(resume_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)