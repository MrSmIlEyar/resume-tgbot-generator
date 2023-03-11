import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from docx import Document
import os

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


@dp.message_handler(commands=["gendoc"])
async def gendoc_command_handler(message: types.Message):
    # запрашиваем у пользователя название файла
    user_id = message.from_user.id

    # создаем пустой документ
    document = Document()

    # сохраняем документ с заданным именем
    filename = f"{user_id}.docx"
    directory = "Documents/"  # замените на свой путь
    filepath = os.path.join(directory, filename)
    document.save(filepath)

    # отвечаем пользователю сообщением об успешном создании файла
    await message.answer(f"Файл {filename} успешно создан.")


# Обработчик команды /send_doc
@dp.message_handler(commands=['send_doc'])
async def send_doc(message: types.Message):
    # Получаем chat_id пользователя
    chat_id = message.chat.id
    user_id = message.from_user.id
    # Получаем путь к файлу docx
    try:
        docx_path = f'Documents/{user_id}.docx'
        # Открываем файл docx в бинарном режиме
        with open(docx_path, 'rb') as docx:
            # Отправляем документ пользователю
            await bot.send_document(chat_id, docx)
    except:
        await message.answer(f"Вашего файла не обнаружено")


# Обработчик текстовых сообщений
@dp.message_handler()
async def echo(message: types.Message):
    # Отправляем эхо-сообщение
    await message.answer(f"Ты написал: {message.text}")


# Запускаем бота
if __name__ == "__main__":
    # executor.start_polling(dp, skip_updates=True)
    executor.start_polling(dp)
