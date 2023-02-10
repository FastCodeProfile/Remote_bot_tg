from loader import dp, bot
from aiogram import types

import time
import os


@dp.message_handler(text=['📈 Консоли'])
async def process_start_cmd_command(message: types.Message):
    await message.answer("🕓 Запуск консолей активирован.\n🟢 Всего будет открыто 50 консолей.\n🟠 С промежутком в 5 секунд.")
    await message.answer_sticker("CAACAgIAAxkBAAED8nxiDC7T9G7ZjQ2o8e7GukIqwhizeAACTQsAAi8P8AYsGupxHe233CME")
    await message.answer("Открыто ✅ 0  из ❌ 50")
    for i in range(1, 50):
        os.system("start")
        await bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 3, text=f"Открыто ✅ {i} из ❌ 50")
        time.sleep(5)
