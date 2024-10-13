import mysql.connector

import constants

db = mysql.connector.connect(
    host=constants.HOST,
    user=constants.USER,
    passwd=constants.PASSWD,
    database=constants.DATABASE,
)

mycursor = db.cursor()


def remove_machine_by_client():
    """Remove all machines in table associated with given client"""
    client = input("Client name to delete: ")
    sql = "DELETE FROM MachineIDs WHERE client_name = %s"
    mycursor.execute(sql, (client,))
    db.commit()


remove_machine_by_client()
