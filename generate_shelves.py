import qrcode

WALLS = ['N']
RACKS = range(1,15)
SLOTS = range(1,64)
delimiter = "-"


def make_qr_code(qr_data):
    qr_code = qrcode.make(qr_data)
    type(qr_code)
    qr_code.save(f"./generated_codes/{qr_data}.png")

for wall in WALLS:
    for rack in RACKS:
        for slot in SLOTS:
            qr_data = (f"{wall}{delimiter}{rack}{delimiter}{slot}")
            make_qr_code(qr_data)