from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📈 Консоли'),
            KeyboardButton(text='📌 Окна'),
            KeyboardButton(text='🖱 Мышка'),
        ],
        [
            KeyboardButton(text='📷 Сделать скриншот'),
            KeyboardButton(text='🔗 Открыть ссылку'),

        ],
        [
            KeyboardButton(text='⚠️ Багаюз'),
        ],
        [
            KeyboardButton(text='❇️ Дополнительно')
        ]
    ],
    resize_keyboard=True
)
