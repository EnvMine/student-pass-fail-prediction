

import pandas as pd

# 1. Load dataset
students = pd.read_csv('students_raw.csv')

# 2. Convert attendance percentage into numbers
students['attendance'] = (
    students['attendance']
    .str.replace('%', '', regex=False)
    .pipe(pd.to_numeric, errors='coerce')
)

# 3. Convert other numerical columns
numeric_columns = [
    'hours_studied',
    'prev_marks',
    'passed'
]

for col in numeric_columns:
    students[col] = pd.to_numeric(
        students[col], errors='coerce'
    )

# 4. Check missing values
print("Missing values in each column:")
print(students.isnull().sum())

print("\nTotal missing values:")
print(students.isnull().sum().sum())

# 5. Check dataset information
print("\nDataset information:")
students.info()

# 6. Check attendance conversion
print("\nFirst 10 attendance values:")
print(students['attendance'].head(10))

students['branch'] = students['branch'].fillna(students['branch'].mode()[0])
students['hours_studied'] = students['hours_studied'].fillna(students['hours_studied'].median())
students['prev_marks'] = students['prev_marks'].fillna(students['prev_marks'].median())

print("Missing values in each column:")
print(students.isnull().sum())
# 7. Prepare features and target variable
X = students[['branch', 'hours_studied', 'attendance', 'prev_marks']]

Y = students['passed']
# convert categorical variable 'branch' into numerical using one-hot encoding
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

preprocessor = ColumnTransformer([
    ('branch', OneHotEncoder(handle_unknown='ignore'), ['branch']),
    ('numbers', StandardScaler(),
     ['hours_studied', 'attendance', 'prev_marks'])
])
# split the dataset into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)
#create machine learning model using logistic regression
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

model = Pipeline([
    ('preprocessing', preprocessor),
    ('classifier', LogisticRegression())
])
#actual learning happens here, the model learns from the training data

model.fit(X_train, Y_train)

predictions = model.predict(X_test)

print("Predicted results:")
print(predictions)

#evaluate model accuracy

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

accuracy = accuracy_score(Y_test, predictions)

print("Students tested:", len(X_test))
print("Accuracy:", accuracy * 100, "%")

#check predictions for some sample students
print("\nConfusion Matrix:")
print(confusion_matrix(Y_test, predictions))

print("\nClassification Report:")
print(classification_report(Y_test, predictions))


# Information about a new student

new_student = pd.DataFrame({
    'branch': ['CSE'],
    'hours_studied': [5],
    'attendance': [73],
    'prev_marks': [72]
})

# Make prediction
prediction = model.predict(new_student)

# Display result
if prediction[0] == 1:
    print("Student is predicted to PASS")
else:
    print("Student is predicted to FAIL")