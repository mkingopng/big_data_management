import pandas as pd
names = [
    'employee_id',
    'first_name',
    'last_name',
    'email',
    'phone_number',
    'hire_date',
    'salary'
    ]

employees_df = pd.read_csv('employees.csv', usecols=[0, 1, 2, 3, 4, 5, 6], names=names)

avg_salary = employees_df['salary'].mean()

print('The average salary is $' + str(round(avg_salary)) + '.')