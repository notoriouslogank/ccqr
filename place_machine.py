import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", passwd="Doge123*", database="testdatabase"
)

mycursor = db.cursor()


def place_machine():
    serial_number = input("Machine to place: ")
    machine_location = input("Machine location: ")
    sql = "UPDATE MachineIDs SET machine_location = %s WHERE serial_number = %s"
    mycursor.execute(sql, (machine_location, serial_number))
    db.commit()


place_machine()
