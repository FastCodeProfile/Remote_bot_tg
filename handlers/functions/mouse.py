from loader import dp
from aiogram import types

import pyautogui


@dp.message_handler(text=['🖱 Мышка'])
async def process_back_command12(message: types.Message):
    await message.answer(f'🕒 Успешно!! \n')
    for i in range(1, 7):
        pyautogui.drag(0, 1500, 3)
