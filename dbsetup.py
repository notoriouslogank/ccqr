import mysql.connector

import constants

if __name__ == "__main__":

    db = mysql.connector.connect(
        host=constants.HOST,
        user=constants.USER,
        passwd=constants.PASSWD,
        database=constants.DATABASE,
    )

    mycursor = db.cursor()

    mycursor.execute(
        "CREATE TABLE MachineMasterList(machine_name VARCHAR(64), client_name VARCHAR(64), serial_number VARCHAR(16), machine_location VARCHAR(10), notes VARCHAR(64), machineID int PRIMARY KEY AUTO_INCREMENT)"
    )
