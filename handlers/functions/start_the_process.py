from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


import subprocess


class Form(StatesGroup):
    start_process = State()


@dp.message_handler(text=['✅ Запустить процесс'])
async def process_start_process_command(message: types.Message):
    await Form.start_process.set()
    await message.answer("⚡️ Название приложения, которое хотите запустить.")


@dp.message_handler(state=Form.start_process)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['start_process'] = message.text

    start_process = subprocess.run(
        ["powershell.exe", "-Command", f"Start-Process -FilePath {data['start_process']}"], stdout=subprocess.PIPE)
    if start_process.returncode == 0:
        await message.answer(f"🕒 Приложение {data['start_process']} успешно запущен.")
    else:
        await message.answer(f"❌ Приложение {data['start_process']} вероятнее всего просто не существует.")
    await state.finish()
