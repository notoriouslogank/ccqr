import sys

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
    serial_number = input("Enter (or scan) machine serial number: ")
    machine_location = input("Enter (or scan) location tag: ")
    sql = "UPDATE MachineMasterList SET machine_location = %s WHERE serial_number = %s"
    mycursor.execute(sql, (machine_location, serial_number))
    db.commit()


def main():
    place_machine()
    place_another = input("Place another? [Y/n]").lower()
    if place_another == "n":
        sys.exit()
    if place_another == "y":
        main()
