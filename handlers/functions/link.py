from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import os


class Form(StatesGroup):
    link = State()


@dp.message_handler(text=['🔗 Открыть ссылку'])
async def process_start_process_command(message: types.Message):
    await Form.link.set()
    await message.answer("⚡️ Введите ссылку на сайт:")


@dp.message_handler(state=Form.link)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['link'] = message.text

    os.system(f"start https://{data['link']}")
    await message.answer("🕡 Успешно")
    await state.finish()
