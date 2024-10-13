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
    """Define location to associate with machine."""
    serial_number = input("Enter (or scan) machine serial number: ")
    machine_location = input("Enter (or scan) location tag: ")
    sql = "UPDATE MachineMasterList SET machine_location = %s WHERE serial_number = %s"
    mycursor.execute(sql, (machine_location, serial_number))
    db.commit()


def another():
    """Ask user whether to enter another machine location or quit the program"""
    add_another = input("Place another machine? [Y/n]").lower()
    if add_another == "n":
        sys.exit()
    if add_another == "y":
        place_machine()


def main():
    place_machine()
    another()
