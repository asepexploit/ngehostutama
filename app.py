"""Entry point: python app.py """

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
