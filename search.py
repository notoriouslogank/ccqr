import mysql.connector
from rich import print as print

import constants

db = mysql.connector.connect(
    host=constants.HOST,
    user=constants.USER,
    passwd=constants.PASSWD,
    database=constants.DATABASE,
)

mycursor = db.cursor()


def search_serial_number():
    """Search table by serial number"""
    serial_number = input("Serial Number: ")
    sql_search = "SELECT * FROM MachineMasterList WHERE serial_number = %s"

    mycursor.execute(sql_search, (serial_number,))

    for x in mycursor:
        print(x)


def search_machine_location():
    """Search table by location tag"""
    location_id = input("Location ID: ")
    sql_search = "SELECT * FROM MachineMasterList WHERE machine_location = %s"
    mycursor.execute(sql_search, (location_id,))

    for x in mycursor:
        print(x)


def search_client():
    """Search table by client name"""
    client_id = input("Client Name: ")
    sql_search = "SELECT * FROM MachineMasterList WHERE client_name = %s"
    mycursor.execute(sql_search, (client_id,))

    for x in mycursor:
        print(x)


def search_all():
    """Show all table entries"""
    sql_search = "SELECT * FROM MachineMasterList"
    mycursor.execute(sql_search)

    for x in mycursor:
        print(x)


def choose_search_parameter():
    """Choose which filter to apply to search"""
    choices = {1: "All Machines", 2: "Serial Number", 3: "Location", 4: "Client"}
    print(f"Filter by: {choices}")
    choice = int(input("Choose an option: "))
    output = choices[choice]

    if output == "Serial Number":
        search_serial_number()
    if output == "Location":
        search_machine_location()
    if output == "Client":
        search_client()
    if output == "All Machines":
        search_all()


def main():
    choose_search_parameter()
