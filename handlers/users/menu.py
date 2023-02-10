from aiogram import types
from loader import dp

from keyboards.default import last_menu


@dp.message_handler(text='❇️ Дополнительно')
async def command_start(message: types.Message):
    await message.answer(f'⌨️ Дополнительное меню', reply_markup=last_menu)
