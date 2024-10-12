import mysql.connector

if __name__ == "__main__":

    db = mysql.connector.connect(
        host="localhost", user="root", passwd="Doge123*", database="testdatabase"
    )

    mycursor = db.cursor()

    mycursor.execute(
        "CREATE TABLE MachineIDs (machine_name VARCHAR(64), client_name VARCHAR(64), serial_number VARCHAR(16), machine_location VARCHAR(10), notes VARCHAR(64), machineID int PRIMARY KEY AUTO_INCREMENT)"
    )
