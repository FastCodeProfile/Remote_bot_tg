from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


import os


class Form(StatesGroup):
    kill_process = State()


@dp.message_handler(text=['❌ Убить процесс'])
async def process_kill_process_command(message: types.Message):
    await Form.kill_process.set()
    await message.answer("🔸 Название процесса, которое хотите уничтожить.")


@dp.message_handler(state=Form.kill_process)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['kill_process'] = message.text

    kill_process = os.system(
        "taskkill /IM " + data['kill_process'] + ".exe" + " -F")
    if kill_process == 0:
        await message.answer(f"🕓 Процесс {data['kill_process']}, успешно уничтожен.")
    else:
        await message.answer(f"❌ Процесс {data['kill_process']} вероятнее всего просто не существует.")
    await state.finish()
