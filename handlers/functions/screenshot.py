from aiogram import types
from loader import dp

import os
from mss import mss


@dp.message_handler(text=['📷 Сделать скриншот'])
async def process_get_photo_command(message: types.Message):
    await message.answer("🕓 Успешно!")
    mss().shot()
    await message.answer_photo(open('monitor-1.png', 'rb'))
    os.remove('monitor-1.png')
