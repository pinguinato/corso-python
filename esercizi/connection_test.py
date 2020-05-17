import mysql.connector

from mysql.connector import errorcode
from datetime import datetime

try:

    print("\nInizio Test di connessione\n")
    connection = mysql.connector.connect(user = 'root', password = 'root', host = '127.0.0.1', database = 'task_manager')
    print("\nMi sono connesso al DB MySql")

    cursorA = connection.cursor()

    cursorA.execute("SELECT * FROM task_manager.task")

    results = cursorA.fetchall()

    print(results)

    for ris in results:
        print(str(ris))

except mysql.connector.Error as err:
   
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\nErrore: problemi con nome utente o password\n")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\nErrore: il database non esiste\n")
   else:
        print("\nErrore: " + err + "\n")

else:
    print("\nChiudo la connessione al DB\n")
    connection.close()
    print("\nConnessione chiusa con successo\n")