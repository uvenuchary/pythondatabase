#Creating a database
import mysql.connector
mydb=mysql.connector.connect(host="localhost",
user="root",
password="")
mycursor=mydb.cursor()
mycursor.execute("create database mydatabase")  