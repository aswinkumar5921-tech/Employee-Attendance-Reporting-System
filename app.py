import pandas as pd
import streamlit as st

db=pd.read_csv("attendance.csv")

st.set_page_config(page_title="Employee Attendance System", layout="wide")
st.title("🏢 Employee Attendance & Reporting System")

print("Hello World")