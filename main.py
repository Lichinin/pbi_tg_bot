from decoder2200 import Decoder2200
from decoder1510 import Decoder1510
import time
import datetime

skopin_decoders2200 = [
    '192.168.1.62',
    '192.168.1.63',
    '192.168.1.64',
    '192.168.1.65',
    # '192.168.1.68',
    '192.168.1.70',
    '192.168.1.72',
]

shilovo_decoders2200 = [
    '192.168.1.112',
    '192.168.1.113',
    '192.168.1.114',
    '192.168.1.115',
    '192.168.1.116',
    '192.168.1.119',
    '192.168.1.121',
]

shilovo_decoders1510 = [
    '192.168.1.120',
    '192.168.1.123',
]

ryazsk_decoders2200 = [
    '192.168.1.162',
    '192.168.1.163',
    '192.168.1.164',
    '192.168.1.165',
    '192.168.1.166',
    '192.168.1.167',
    '192.168.1.172',
]

ryazsk_decoders1510 = [
    '192.168.1.171',
]

korablino_decoders2200 = [
    '192.168.1.212',
    '192.168.1.213',
    '192.168.1.214',
    '192.168.1.215',
    '192.168.1.216',
    '192.168.1.217',
    '192.168.1.218',
]

korablino_decoders1510 = [
    # '192.168.1.221',
]


if __name__ == '__main__':
    while True:
        print(f'----- Старт проверки {datetime.datetime.now()} -----')

        for ip in skopin_decoders2200:
            pbi = Decoder2200(ip, 'SKOPIN_PASS', 'Скопин')
            pbi.check_status()

        for ip in shilovo_decoders2200:
            pbi = Decoder2200(ip, 'SHILOVO_PASS', 'Шилово')
            pbi.check_status()

        for ip in shilovo_decoders1510:
            pbi = Decoder1510(ip, 'SHILOVO_PASS', 'Шилово')
            pbi.check_status()

        for ip in ryazsk_decoders2200:
            pbi = Decoder2200(ip, 'RYAZSK_PASS', 'Ряжск')
            pbi.check_status()

        for ip in ryazsk_decoders1510:
            pbi = Decoder1510(ip, 'RYAZSK_PASS', 'Ряжск')
            pbi.check_status()

        for ip in korablino_decoders2200:
            pbi = Decoder2200(ip, 'KORABLINO_PASS', 'Кораблино')
            pbi.check_status()

        for ip in korablino_decoders1510:
            pbi = Decoder1510(ip, 'KORABLINO_PASS', 'Кораблино')
            pbi.check_status()

        print(f'-----Проверка завершена {datetime.datetime.now()} -----')

        time.sleep(10)
