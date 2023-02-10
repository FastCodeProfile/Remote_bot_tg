from loader import dp
from aiogram import types


import psutil
from collections import Counter


@dp.message_handler(text=['🗒 Получить процессы'])
async def process_get_process_command(message: types.Message):
    list_porocess = []
    for p in psutil.process_iter():
        list_porocess.append(p.name())

    clear_list_process = sorted(
        Counter(list_porocess), key=lambda w: w.lower())
    await message.answer(f"♻️ Активные процессы:")
    await message.answer('\n'.join(clear_list_process))
