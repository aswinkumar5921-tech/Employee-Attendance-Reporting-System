import pandas as pd

df=pd.read_csv("attendance.csv")

df["check_in"]=pd.to_datetime(df["check_in"])
df["check_out"]=pd.to_datetime(df["check_out"])

r=df.groupby("employee_name").size()
print(r)

r1=23-r
print(r1)

result = (df.assign(late=(df["check_in"] > "9:15")).groupby("employee_name")["late"].sum())
print(result) 

df["hours"] = (df["check_out"] - df["check_in"]).dt.total_seconds()/3600
result = df.groupby("employee_name")["hours"].mean().round(2)
print(result)

max1=r.max()
print(r[r==max1])

max2=r1.max()
print(r1[r1==max2])

result = (df.assign(early=(df["check_out"] < "18:00")).groupby("employee_name")["early"].sum())
print(result) 

r=df[df["employee_name"].str.startswith("A")]
print(r["employee_name"].unique())

r=df[df["employee_name"].str.contains("r") & df["employee_name"].str.contains("s")]
print(r["employee_name"].unique())

r=df[df["date"]=="6/9/2026"]
print(r["employee_name"].unique())