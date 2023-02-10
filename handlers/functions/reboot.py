from aiogram import types
from loader import dp

import os


@dp.message_handler(text=['♻️ Перезагрузить компьютер'])
async def process_back_command(message: types.Message):
    os.system('shutdown -r /t 0 /f')
    await message.answer("🕓 Перезагрузка компьютера...")
    await message.answer_sticker("CAACAgIAAxkBAAED8nxiDC7T9G7ZjQ2o8e7GukIqwhizeAACTQsAAi8P8AYsGupxHe233CME")
