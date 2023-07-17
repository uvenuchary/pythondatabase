#Table creation
import mysql.connector
mydb=mysql.connector.connect(host="localhost",
user="root",
password="",
database="mydatabase")
mycursor=mydb.cursor()
mycursor.execute("create table emp(name varchar(255),dept varchar(255))")