#Display all the records entered into the table
import mysql.connector
mydb=mysql.connector.connect(host="localhost",
user="root",
password="",
database="mydatabase")
mycursor=mydb.cursor()
mycursor.execute("select * from emp")
result=mycursor.fetchall()
#fetchall takes all records.
for x in result:
    print(x)  
    