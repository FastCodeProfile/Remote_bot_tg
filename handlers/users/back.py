from aiogram import types
from loader import dp

from keyboards.default import start_menu


@dp.message_handler(text='Вернуться 🔙')
async def command_start(message: types.Message):
    await message.answer(f'Вернулись {message.from_user.full_name} \n', reply_markup=start_menu)
