import pandas as pd
students= pd.read_csv('students_raw.csv')
students['attendance'] = pd.to_numeric(
    students['attendance'], errors='coerce'
)
print(students.dtypes)
#this is the rule i invented
def willpass(student_name,branch,hours_studied,attendance,prev_marks):
    if hours_studied>5 and attendance>75:
        return 1
    return 0

#let see how often this rule is correct
correct=0
for _, row in students.iterrows():
    my_answer=willpass(row.student_name,row.branch,row.hours_studied,row.attendance,row.prev_marks)
    real_answer=row.passed
    if my_answer==real_answer:
        correct+=1

print('students checked:',len(students))
print('correct predictions:',correct)
print('accuracy:',correct/len(students)*100,'%')

# New student information

new_student = {
    'student_name': 'Rahul',
    'branch': 'CSE',
    'hours_studied': 5,
    'attendance': 73,
    'prev_marks': 72
}

# Apply our manually created rule

prediction = willpass(
    new_student['student_name'],
    new_student['branch'],
    new_student['hours_studied'],
    new_student['attendance'],
    new_student['prev_marks']
)

# Display result

if prediction == 1:
    print("Student is predicted to PASS")
else:
    print("Student is predicted to FAIL")