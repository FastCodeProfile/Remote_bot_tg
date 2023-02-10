import os
import logging
import requests
import platform

from loader import bot
from aiogram import Dispatcher
from data.config import admins_id


async def on_startup_notify(dp: Dispatcher):
    try:
        req = requests.get('http://ip.42.pl/raw')
        ip = req.text
        uname = os.getlogin()
        processor = platform.processor()
        os_system = platform.system()
        os_version = platform.release()
        for admin_id in admins_id:
            await bot.send_message(chat_id=admin_id, text=f"🔴 IP-Адрес: {ip}\n🟠 Название PC: {uname}\n🟡 Операционная система: {os_system} {os_version}\n🟢 Процессор: {processor}")

    except Exception as err:
        logging.exception(err)
