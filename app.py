import mysql.connector
import os
import time

time.sleep(20)
mydb = mysql.connector.connect(
        host= os.environ.get('DB_HOST'),
    user="root",
    password="admin123",
    port = 3306
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS PROBA")
mycursor.execute("USE PROBA")
print("proba")
mycursor.execute("CREATE TABLE IF NOT EXISTS TABLAPROBA(id int, PRIMARY KEY(id))")
print("proba table")


mydb.commit()
