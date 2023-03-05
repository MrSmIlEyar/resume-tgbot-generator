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
    await message.answer("Привет! Я бот, который может отвечать на твои сообщения.")

# Обработчик текстовых сообщений
@dp.message_handler()
async def echo(message: types.Message):
    # Отправляем эхо-сообщение
    await message.answer(f"Ты написал: {message.text}")

# Запускаем бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
