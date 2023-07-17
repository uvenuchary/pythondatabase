#Entering multiple values into table
import mysql.connector
mydb=mysql.connector.connect(host="localhost",
user="root",
password="",
database="mydatabase")
mycursor=mydb.cursor()
sql="insert into emp(name,dept)values(%s,%s)"
val=[
    ("prabhas","marketing"),
    ("ntr","accounts"),
    ("balayya","transport"),
    ("ssr","administration") 
]
mycursor.executemany(sql,val)
mydb.commit() 
print(mycursor.rowcount,"was inserted")
