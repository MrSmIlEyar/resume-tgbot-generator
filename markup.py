from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# кнопки для пользователя
ButtonGetResume = KeyboardButton("Получить резюме")
ButtonEditInfo = KeyboardButton("Изменить информацию о себе")
ButtonProfile = KeyboardButton("Профиль")
ButtonQuiz = KeyboardButton("Рассказать о себе")

# кнопка возвращения в главное меню
MainMenuButton = KeyboardButton("Главное меню")
BackButton = KeyboardButton("Назад")

# кнопки редактирования информации
EditPhotoButton = KeyboardButton("Изменить фото")
EditTextButton = KeyboardButton("Изменить текст")


EditInfo = ReplyKeyboardMarkup(resize_keyboard=True).add(EditTextButton, EditPhotoButton, MainMenuButton)
EditPhoto = ReplyKeyboardMarkup(resize_keyboard=True).add(ButtonEditInfo)
EditText = ReplyKeyboardMarkup(resize_keyboard=True).add(ButtonEditInfo)
Profile = ReplyKeyboardMarkup(resize_keyboard=True).add(MainMenuButton)
MainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(ButtonGetResume, ButtonProfile, ButtonQuiz, ButtonEditInfo)