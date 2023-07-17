#Displaying the filtered values 
import mysql.connector
mydb=mysql.connector.connect(host="localhost",
user="root",
password="",
database="mydatabase")
mycursor=mydb.cursor()
mycursor.execute("select * from emp where dept ='accounts'")
result=mycursor.fetchall()
#fetchall takes all records.
for x in result:
    print(x)

