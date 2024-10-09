import csv
from datetime import date

import qrcode


def get_machine_name():
    machine_name = input("Machine ID: ")
    machine_id = machine_name.upper()
    return machine_id


def get_client_info(machine_id):
    client_name = input("Name: ")
    mac_address = input("MAC Address: ")
    timestamp = date.today()
    return machine_id, client_name, mac_address, timestamp


def write_csv(qr_data):
    with open("./csv/master_list.csv", "a", newline="") as csvfile:
        writer = csv.writer(
            csvfile, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow(qr_data)


def make_qr_code(qr_data):
    qr_code = qrcode.make(qr_data)
    type(qr_code)
    qr_code.save(f"./qr/machine_id/{machine_id}.png")


machine_id = get_machine_name()
write_csv(get_client_info(machine_id))
make_qr_code(machine_id)
