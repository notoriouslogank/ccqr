import mysql.connector
import qrcode

import constants


def create_qr(serial_number):
    qr_code = qrcode.make(serial_number)
    type(qr_code)
    qr_code.save(f"./qr/machine/{serial_number}.png")


def main():
    while True:
        db = mysql.connector.connect(
            host=constants.HOST,
            user=constants.USER,
            passwd=constants.PASSWD,
            database=constants.DATABASE,
        )

        mycursor = db.cursor()
        machine_name = input("Machine Name: ")
        client_name = input("Client Name: ")
        serial_number = input("Serial Number: ")
        machine_location = input("Location: ")
        notes = input("Notes: ")
        mycursor.execute(
            "INSERT INTO MachineMasterList (machine_name, client_name, serial_number, machine_location, notes) VALUES (%s,%s,%s,%s,%s)",
            (
                f"{machine_name}",
                f"{client_name}",
                f"{serial_number}",
                f"{machine_location}",
                f"{notes}",
            ),
        )
        db.commit()
        create_qr(serial_number=serial_number)

        add_another = input("Add another? [Y/n] ").lower()
        if add_another == "n":
            exit()
        if add_another == "Y":
            pass
