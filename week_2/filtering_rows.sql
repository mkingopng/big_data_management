-- Filtering Rows
-- You can select only certain rows by adding example_file_statistics WHERE clause to your query.

-- The following query selects employees whose salary is greater than $10,000.
SELECT employee_id, last_name, first_name, salary, hire_date
FROM employees
WHERE salary > 10000;

-- The following query selects employees whose last name is "King".
SELECT employee_id, last_name, first_name, salary, hire_date
FROM employees
WHERE last_name = 'King';

-- The following query selects employees who were hired on or before 8th March 2008.
SELECT employee_id, last_name, first_name, salary, hire_date
FROM employees
WHERE hire_date <= '2008-03-08';

-- When filtering string or date columns you should use quotes around the filtering value, but not for numeric columns.
-- For dates, make sure you are aware of the format in which dates are stored. In MySQL the default is YYYY-MM-DD
-- (e.g. 2011-01-16). In Oracle it is DD-MON-YY (e.g. 16-JAN-11).

-- Filtering strings is NOT case sensitive in MySQL - filtering by 'King' produces the same results as filtering by
-- 'KING'. Be aware that in some versions of SQL the filtering is case sensitive.
SELECT employee_id, last_name, first_name
FROM employees
WHERE last_name = 'King';

SELECT employee_id, last_name, first_name
FROM employees
WHERE last_name = 'KING';

