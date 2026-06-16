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
mycursor.execute("SELECT employee_name,COUNT(*) AS attendance_count FROM attendance GROUP BY employee_name")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
mycursor.execute("SELECT employee_name, (23 - COUNT(*)) AS absences FROM attendance GROUP BY employee_name")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.execute("SELECT employee_name,SUM(CASE WHEN check_in > '9:15' THEN '1' ELSE '0' END) AS late_count FROM attendance GROUP BY employee_name")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
mycursor.execute("SELECT employee_name,ROUND(AVG(TIMESTAMPDIFF(MINUTE,STR_TO_DATE(check_in,'%H:%i'),STR_TO_DATE(check_out,'%H:%i')))/60,2) AS avg_hours FROM attendance GROUP BY employee_name")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.execute("SELECT employee_name,COUNT(*) AS days_worked FROM attendance GROUP BY employee_name HAVING COUNT(*) = ( SELECT MAX(days_worked) FROM (SELECT COUNT(*) AS days_worked FROM attendance GROUP BY employee_name) AS Attendance)")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.execute("SELECT employee_name,(23 - COUNT(*)) AS absences FROM attendance GROUP BY employee_name HAVING COUNT(*) = ( SELECT MIN(absences_count) FROM (SELECT COUNT(*) AS absences_count FROM attendance GROUP BY employee_name) AS Absences)")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.execute("SELECT employee_name,SUM(CASE WHEN check_out < '18:00' THEN '1' ELSE '0' END) AS late_count FROM attendance GROUP BY employee_name")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.execute("SELECT DISTINCT employee_name FROM attendance WHERE employee_name LIKE 'A%'")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
mycursor.execute("SELECT DISTINCT employee_name FROM attendance WHERE employee_name LIKE '%r%' AND employee_name LIKE '%s%'")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
mycursor.execute("SELECT employee_name FROM attendance WHERE date = '6/9/2026'")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
