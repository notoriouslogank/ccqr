import mysql.connector
from rich import print as print

db = mysql.connector.connect(
    host="localhost", user="root", passwd="Doge123*", database="testdatabase"
)


def search_serial_number():
    mycursor = db.cursor()
    serial_number = input("Serial Number: ")
    sql_search = "SELECT * FROM MachineIDs WHERE serial_number = %s"

    mycursor.execute(sql_search, (serial_number,))

    for x in mycursor:
        print(x)


def search_machine_location():
    mycursor = db.cursor()
    location_id = input("Location ID: ")
    sql_search = "SELECT * FROM MachineIDs WHERE machine_location = %s"
    mycursor.execute(sql_search, (location_id,))

    for x in mycursor:
        print(x)


def search_client():
    mycursor = db.cursor()
    client_id = input("Client Name: ")
    sql_search = "SELECT * FROM MachineIDs WHERE client_name = %s"
    mycursor.execute(sql_search, (client_id,))

    for x in mycursor:
        print(x)


def search_all():
    mycursor = db.cursor()
    sql_search = "SELECT * FROM MachineIDs"
    mycursor.execute(sql_search)

    for x in mycursor:
        print(x)


def choose_search_parameter():
    search_param = input(
        "Choose search parameter: [A]ll Machines; [S]erial Number; [L]ocation; [C]lient "
    ).lower()
    if search_param == "s":
        search_serial_number()
    if search_param == "l":
        search_machine_location()
    if search_param == "c":
        search_client()
    if search_param == "a":
        search_all()


choose_search_parameter()
