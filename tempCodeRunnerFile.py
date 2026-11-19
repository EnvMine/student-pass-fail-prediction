import pandas as pd

# students = pd.read_csv('students_raw.csv')

# # Convert numerical columns
# numeric_columns = [
#     'hours_studied',
#     'attendance',
#     'prev_marks',
#     'passed'
# ]

# for col in numeric_columns:
#     students[col] = pd.to_numeric(
#         students[col], errors='coerce'
#     )

# # Check missing values
# print("Missing values in each column:")
# print(students.isnull().sum())

# print("\nTotal missing values:")
# print(students.isnull().sum().sum())

# print("\nDataset information:")
# print(students.info())