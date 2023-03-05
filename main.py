import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Задаем уровень логов
logging.basicConfig(level=logging.INFO)

# Создаем объект бота
bot = Bot(token="6137850721:AAFSamidQjOex0cjEF5G1SYqtj1knbeZHz8")

# Создаем объект диспетчера
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет, я напишу твоё резюме, только лишь расскажи о себе)")


@dp.message_handler(commands=["get_resume"])
async def resume(message: types.Message):
    await message.answer("Здесь будет резюме")


@dp.message_handler(commands=["edit_info"])
async def resume(message: types.Message):
    await message.answer("Здесь можно изменить информацию о себе")


@dp.message_handler(commands=["profile"])
async def resume(message: types.Message):
    await message.answer("Здесь можно увидеть информацию о себе")

@dp.message_handler()
async def main_dialog(message: types.Message):
    await message.answer("Мне нужны команды...")


# Запускаем бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
