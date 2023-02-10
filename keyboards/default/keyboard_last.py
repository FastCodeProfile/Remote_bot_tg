from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

last_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗒 Получить процессы'),
            KeyboardButton(text='❌ Убить процесс'),
            KeyboardButton(text='✅ Запустить процесс'),
        ],
        [
            KeyboardButton(text='📝 Диалог'),
        ],
        [
            KeyboardButton(text='♻️ Перезагрузить компьютер'),
            KeyboardButton(text='📟 Explorer'),
            KeyboardButton(text='Ⓜ️ Синий экран смерти'),
        ],
        [
            KeyboardButton(text='Вернуться 🔙')
        ],
    ],
    resize_keyboard=True
)
