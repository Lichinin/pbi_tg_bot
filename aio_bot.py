import asyncio
import datetime
import logging

from dotenv import load_dotenv

from bot import Aiobot
from decoder2200 import Decoder2200

load_dotenv()

shilovo_decoders2200 = [
    '192.168.1.112',
    '192.168.1.113',
    '192.168.1.114',
    '192.168.1.115',
    '192.168.1.116',
    '192.168.1.119',
    '192.168.1.121',
]

logging.basicConfig(level=logging.INFO)


async def periodic_checks():
    while True:
        print(f'----- Старт проверки {datetime.datetime.now()} -----')

        for ip in shilovo_decoders2200:
            pbi = Decoder2200(ip, 'SHILOVO_PASS', 'Шилово')
            await pbi.check_status()

        print(f'-----Проверка завершена {datetime.datetime.now()} -----')

        await asyncio.sleep(60)


async def main():
    aiobot = Aiobot()
    await asyncio.gather(
        aiobot.run_bot(),
        periodic_checks(),
    )

if __name__ == '__main__':
    asyncio.run(main())
