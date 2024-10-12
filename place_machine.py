import mysql.connector

import constants

db = mysql.connector.connect(
    host=constants.HOST,
    user=constants.USER,
    passwd=constants.PASSWD,
    database=constants.DATABASE,
)

mycursor = db.cursor()


def place_machine():
    serial_number = input("Machine to place: ")
    machine_location = input("Machine location: ")
    sql = "UPDATE MachineIDs SET machine_location = %s WHERE serial_number = %s"
    mycursor.execute(sql, (machine_location, serial_number))
    db.commit()


def main():
    place_machine()
