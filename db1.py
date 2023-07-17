#To display the list of databases
import mysql.connector
mydb=mysql.connector.connect(host="localhost",
user="root",
password="")
mycursor=mydb.cursor()
mycursor.execute("show databases")
for x in mycursor:
    print(x)
    