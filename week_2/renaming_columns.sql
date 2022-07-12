-- renaming COLUMNS
SELECT
    employee_id AS Employee,
    employee_id AS "Employee Id",
    last_name Surname,
    first_name "First Name"
FROM employees;

-- Try selecting the department id and name columns from the departments table, calling the first column "Id" and the
-- second column "Department name":
SELECT
    department_id AS "id",
    department_name AS "Department Name"
FROM departments;
