"""Entry point: python app.py

File ini sengaja tetap plain-text (tidak dikompilasi) -- logic sebenarnya ada di
paket checker/ yang dikompilasi jadi checker.pyd. Import checker di baris pertama
otomatis memicu enforce_license() (lihat checker/__init__.py), sebelum apa pun lain
sempat jalan.
"""

import asyncio

from checker.core import main
from colorama import Fore

if __name__ == "__main__":
    try:
        # Menghapus workaround WindowsSelectorEventLoopPolicy karena Playwright
        # membutuhkan ProactorEventLoop (bawaan Windows sejak Python 3.8+).
        # Workaround tersebut memicu error NotImplementedError saat membuat subprocess.
        asyncio.run(main())
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Script dihentikan secara paksa oleh pengguna.")
