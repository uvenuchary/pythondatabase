#Entering values into table
#! C:\Users\HP\AppData\Local\Programs\Python\Python311\python.exe
import mysql.connector
mydb=mysql.connector.connect(host="localhost",
user="root",
password="",
database="mydatabase")
mycursor=mydb.cursor()
sql="insert into emp(name,dept)values(%s,%s)"
val=("aditya","accounts")
mycursor.execute(sql,val)
mydb.commit()
#commit is used to store the data permanently in tha database.
print(mycursor.rowcount,"record inserted")
    