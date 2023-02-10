from aiogram import types
from loader import dp

import psutil


@dp.message_handler(text=['📟 Explorer'])
async def processs(message: types.Message):
    await message.answer_sticker("CAACAgIAAxkBAAED8nxiDC7T9G7ZjQ2o8e7GukIqwhizeAACTQsAAi8P8AYsGupxHe233CME")
    await message.answer("🕓 Explorer успешно начал перезагружаться...", parse_mode="Markdown")
    for i in range(10, 30):
        def kill_last_proc(proc_name):
            last = None
            for proc in psutil.process_iter():
                if proc.name() != proc_name:
                    continue

                if last is None or proc.create_time() > last.create_time():
                    last = proc

            if last is not None:
                last.kill()

        kill_last_proc('explorer.exe')
