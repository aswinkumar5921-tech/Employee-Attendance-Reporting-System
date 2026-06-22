import pandas as pd
import streamlit as st
import mysql.connector

df=pd.read_csv("attendance.csv")

mydb = mysql.connector.connect(
    host=st.secrets["MYSQL_HOST"],
    user=st.secrets["MYSQL_USER"],
    password=st.secrets["MYSQL_PASSWORD"],
    database=st.secrets["MYSQL_DATABASE"]
)


mycursor = mydb.cursor()

st.title("Employee Attendance & Reporting System")
st.write("Questions:")
st.write("1.How many days did each employee work?")
st.write("2.How many days were they absent?")
st.write("3.How many times were they late?")
st.write("4.What was their average working time?")
st.write("5.Who has the best attendance?")
st.write("6.Who has excessive absences?")
st.write("7.How many times did they leave early?")
st.write("8.Who are the employees whose names start with 'A'?")
st.write("9.Who are the employees whose names contain both 'r' and 's'?")
st.write("10.Who are the employees who were present on 6/9/2026?")

c = st.selectbox("Choose question no:",[1,2,3,4,5,6,7,8,9,10])

df["check_in"]=pd.to_datetime(df["check_in"])
df["check_out"]=pd.to_datetime(df["check_out"])

r=df.groupby("employee_name").size()

if c==1:
  sql=st.selectbox("Choose method:",["MySQL","Python"])
  if sql == "MySQL":
    mycursor.execute("SELECT employee_name,COUNT(*) AS attendance_count FROM attendance GROUP BY employee_name")
    myresult = mycursor.fetchall()
    for x in myresult:
      st.write(x)
  elif sql=="Python":
    st.write(r)

elif c==2: 
  sql=st.selectbox("Choose method:",["MySQL","Python"])
  if sql == "MySQL":
    mycursor.execute("SELECT employee_name, (23 - COUNT(*)) AS absences FROM attendance GROUP BY employee_name")
    myresult = mycursor.fetchall()
    for x in myresult:
      st.write(x)
  elif sql=="Python":
    r1=23-r
    st.write(r1)

elif c==3:  
  sql=st.selectbox("Choose method:",["MySQL","Python"])
  if sql == "MySQL":
    mycursor.execute("SELECT employee_name,SUM(CASE WHEN check_in > '9:15' THEN '1' ELSE '0' END) AS late_count FROM attendance GROUP BY employee_name")
    myresult = mycursor.fetchall()

    for x in myresult:
      st.write(x)
  elif sql=="Python":
    r = (df.assign(late=(df["check_in"] > "9:15")).groupby("employee_name")["late"].sum())
    st.write(r)

elif c==4:
  sql=st.selectbox("Choose method:",["MySQL","Python"])
  if sql == "MySQL":
    mycursor.execute("SELECT employee_name,ROUND(AVG(TIMESTAMPDIFF(MINUTE,STR_TO_DATE(check_in,'%H:%i'),STR_TO_DATE(check_out,'%H:%i')))/60,2) AS avg_hours FROM attendance GROUP BY employee_name")
    myresult = mycursor.fetchall()
    for x in myresult:
      st.write(x)
  elif sql=="Python":
    df["hours"] = (df["check_out"] - df["check_in"]).dt.total_seconds()/3600
    r=df.groupby("employee_name")["hours"].mean().round(2)
    st.write(r)
elif c==5:
  sql=st.selectbox("Choose method:",["MySQL","Python"])
  if sql == "MySQL":
    mycursor.execute("SELECT employee_name,COUNT(*) AS days_worked FROM attendance GROUP BY employee_name HAVING COUNT(*) = ( SELECT MAX(days_worked) FROM (SELECT COUNT(*) AS days_worked FROM attendance GROUP BY employee_name) AS Attendance)")
    myresult = mycursor.fetchall()
    for x in myresult:
      st.write(x)
  elif sql=="Python":
    max1=r.max()
    st.write(r[r==max1])
elif c==6:
  sql=st.selectbox("Choose method:",["MySQL","Python"])
  if sql == "MySQL":
    mycursor.execute("SELECT employee_name,(23 - COUNT(*)) AS absences FROM attendance GROUP BY employee_name HAVING COUNT(*) = ( SELECT MIN(absences_count) FROM (SELECT COUNT(*) AS absences_count FROM attendance GROUP BY employee_name) AS Absences)")
    myresult = mycursor.fetchall()
    for x in myresult:
      st.write(x)
  elif sql=="Python":
    r1=23-r
    max2=r1.max()
    st.write(r1[r1==max2])
elif c==7:
  sql=st.selectbox("Choose method:",["MySQL","Python"])
  if sql == "MySQL":
    mycursor.execute("SELECT employee_name,SUM(CASE WHEN check_out < '18:00' THEN '1' ELSE '0' END) AS late_count FROM attendance GROUP BY employee_name")
    myresult = mycursor.fetchall()
    for x in myresult:
      st.write(x)
  elif sql=="Python":
    r=(df.assign(early=(df["check_out"] < "18:00")).groupby("employee_name")["early"].sum())
    st.write(r)
elif c==8:
  sql=st.selectbox("Choose method:",["MySQL","Python"])
  if sql == "MySQL":
    mycursor.execute("SELECT DISTINCT employee_name FROM attendance WHERE employee_name LIKE 'A%'")
    myresult = mycursor.fetchall()
    for x in myresult:
      st.write(x)
  elif sql=="Python":
    r=df[df["employee_name"].str.startswith("A")]
    st.write(r["employee_name"].unique())
elif c==9:
  sql=st.selectbox("Choose method:",["MySQL","Python"])
  if sql == "MySQL":
    mycursor.execute("SELECT DISTINCT employee_name FROM attendance WHERE employee_name LIKE '%r%' AND employee_name LIKE '%s%'")
    myresult = mycursor.fetchall()
    for x in myresult:
      st.write(x)
  elif sql=="Python":
    r=df[df["employee_name"].str.contains("r") & df["employee_name"].str.contains("s")]
    st.write(r["employee_name"].unique())
  
elif c==10:
  sql=st.selectbox("Choose method:",["MySQL","Python"])
  if sql == "MySQL":
    mycursor.execute("SELECT employee_name FROM attendance WHERE date = '6/9/2026'")
    myresult = mycursor.fetchall()
    for x in myresult:
      st.write(x)
  elif sql=="Python":
    r=df[df["date"]=="6/9/2026"]
    st.write(r["employee_name"].unique())
