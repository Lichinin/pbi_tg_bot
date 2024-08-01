from decoder import Decoder2200

shilovo_decoders = [
    '192.168.1.112',
    '192.168.1.113',
    '192.168.1.114',
    '192.168.1.115',
    '192.168.1.116',
    '192.168.1.119',
    '192.168.1.121',
]
for ip in shilovo_decoders:
    pbi = Decoder2200(ip, 'SHILOVO_PASS', 'Шилово')
    pbi.check_status()
