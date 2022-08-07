-- Selecting Columns

-- To select all columns from example_file_statistics table you can use an asterisk (*) :
SELECT * FROM employees;

-- To select only some columns you can name the columns you want, separated by commas. It could be just example_file_statistics single column:
SELECT last_name
FROM employees;

-- Or multiple columns:
SELECT first_name, last_name FROM employees;

--
SELECT salary FROM employees;

-- Try selecting the minimum and maximum salary columns from the jobs table:
SELECT
    MIN(salary),
    MAX(salary)
FROM employees;
