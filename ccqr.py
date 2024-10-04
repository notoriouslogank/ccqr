import csv
from datetime import date

import qrcode


def get_client_info():

    name = input("Name: ")
    serial_number = input("Serial Number: ")
    mac_address = input("MAC Address: ")
    rack = input("Rack: ")
    port = input("Port: ")
    timestamp = date.today()
    return name, serial_number, mac_address, rack, port, timestamp


def write_csv(qr_data):
    with open("master_list.csv", "a", newline="") as csvfile:
        writer = csv.writer(
            csvfile, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow(qr_data)


def make_qr_code(qr_data):
    qr_code = qrcode.make(qr_data)
    type(qr_code)
    qr_code.save("qr_code.png")


qr_data = get_client_info()
write_csv(qr_data)
make_qr_code(qr_data)
