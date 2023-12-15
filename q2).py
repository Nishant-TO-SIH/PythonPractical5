import mysql.connector as mysql

user="root"
password="Root123"
address = "localhost"

conn = mysql.connect(user=user,password=password,address=address)
cur=conn.cursor()

cur.execute("SELECT * from table1")
a=cur.fetchall()

print(a)