from aiogram import types
from loader import dp

import subprocess
import os


@dp.message_handler(text=['⚠️ Багаюз'])
async def processs(message: types.Message):
    await message.answer_sticker("CAACAgIAAxkBAAED8nxiDC7T9G7ZjQ2o8e7GukIqwhizeAACTQsAAi8P8AYsGupxHe233CME")
    await message.answer("🕓 Успешно!", parse_mode="Markdown")
    for i in range(0, 5):
        subprocess.run(["powershell.exe", "-Command", f"Start-Process -FilePath msedge.exe"],
                       stdout=subprocess.PIPE)
        subprocess.run(["powershell.exe", "-Command",
                       f"Start-Process -FilePath cmd.exe"], stdout=subprocess.PIPE)
        subprocess.run(["powershell.exe", "-Command", f"Start-Process -FilePath notepad.exe"],
                       stdout=subprocess.PIPE)
        subprocess.run(["powershell.exe", "-Command", f"Start-Process -FilePath mspaint.exe"],
                       stdout=subprocess.PIPE)
        subprocess.run(["powershell.exe", "-Command", f"Start-Process -FilePath soffice.exe"],
                       stdout=subprocess.PIPE)
        subprocess.run(["powershell.exe", "-Command", f"Start-Process -FilePath WinRAR.exe"],
                       stdout=subprocess.PIPE)
        os.system("taskkill /IM msedge.exe")
        os.system("taskkill /IM cmd.exe")
        os.system("taskkill /IM notepad.exe")
        os.system("taskkill /IM mspaint.exe")
        os.system("taskkill /IM soffice.exe")
        os.system("taskkill /IM WinRAR.exe")
