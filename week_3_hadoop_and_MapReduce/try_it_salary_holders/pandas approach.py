import pandas as pd

employees = pd.read_csv('employees.csv', header=None)
employees.columns = [
    'employee_id',
    'first_name',
    'last_name',
    'email',
    'phone_number',
    'hire_date',
    'salary'
]

# salary = employees['salary'].unique()

employees_new = employees[['salary', 'last_name']].groupby(['salary'])['last_name'].apply(', '.join).reset_index()

print(employees_new)
