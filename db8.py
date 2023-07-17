#Entering values into table and displaying the entered records in table.
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
mycursor.execute("select * from emp")
result=mycursor.fetchall()
#fetchall takes all records.
for x in result:
    print(x)
    