# Employee Attendance & Reporting System
## Project Overview

This project analyzes employee attendance data using both Python (Pandas) and SQL (SQLite) or MySQL in localhost.
The application allows users to choose between Python-based and SQL-based solutions for generating attendance reports through a Streamlit interface.

---

## Technologies Used

- Python
- Pandas
- SQLite3
- Streamlit
- AWS S3 (Cloud Storage)

---

## Dataset

The dataset contains the following columns:

- employee_id
- employee_name
- date
- check_in
- check_out

---

## Reports Available

1. Days Worked by Each Employee
2. Days Absent by Each Employee
3. Late Count
4. Average Working Hours
5. Best Attendance
6. Excessive Absences
7. Early Leave Count
8. Employees Whose Names Start With 'A'
9. Employees Whose Names Contain Both 'R' and 'S'
10. Employees Present on 6/9/2026

---

## Features

- Python implementation using Pandas
- SQL implementation using SQLite
- Streamlit user interface
- Cloud-hosted dataset using AWS S3
- Interactive report selection

---

## Installation

Install required packages:

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Project Structure

```text
├── app.py
├── requirements.txt
├── mysql_app.py
├──local_app.py
├── README.md
└── attendance.csv
```

---

## Author

Aswin
