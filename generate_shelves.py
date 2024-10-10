import qrcode

wrs = []  # literally "walls, racks, slots" as a list


def get_delimiter():
    delimiter = input("Delimiter: ")
    return delimiter


def get_shelf_information():
    walls = input("Wall Letter: ")
    racks = range(
        1, int(input("Racks to create: ")) + 1
    )  # Accounting for the off-by-one error due to zero indexing
    slots = range(1, int(input("Slots in rack: ")) + 1)  # See above
    wrs.append(walls)
    wrs.append(racks)
    wrs.append(slots)


def make_qr_code(qr_data):
    qr_code = qrcode.make(qr_data)
    type(qr_code)
    qr_code.save(f"./qr/location/{qr_data}.png")


def main():
    get_shelf_information()
    delimiter = get_delimiter()
    for wall in wrs[0]:
        for rack in wrs[1]:
            for slot in wrs[2]:
                qr_data = f"{wall}{delimiter}{rack}{delimiter}{slot}"
                make_qr_code(qr_data)
