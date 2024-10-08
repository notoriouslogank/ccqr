import csv
from datetime import date

import qrcode

serial_number = input("Serial number: ")

def sanitize_output(input):
    output = str(input).capitalize()
    return output

def get_client_info():

    client_name = sanitize_output(input("Name: "))
    mac_address = sanitize_output(input("MAC Address: "))
    timestamp = date.today()
    return client_name, mac_address, timestamp


def write_csv(qr_data):
    with open("master_list.csv", "a", newline="") as csvfile:
        writer = csv.writer(
            csvfile, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow(qr_data)


def make_qr_code(qr_data):
    qr_code = qrcode.make(qr_data)
    type(qr_code)
    qr_code.save(f"{sanitize_output(serial_number)}.png")


qr_data = get_client_info()
write_csv(qr_data)
make_qr_code(qr_data)
