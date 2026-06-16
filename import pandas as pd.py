import pandas as pd
import mysql.connector

db=pd.read_csv("attendance.csv")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aswin123*",
    database="attendance_db"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT employee_name,SUM(CASE WHEN check_out < '18:00' THEN '1' ELSE '0' END) AS late_count FROM attendance GROUP BY employee_name")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
