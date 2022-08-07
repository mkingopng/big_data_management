-- Grouping rows

-- When using aggregate functions to get totals you typically want the totals for groups of rows, not for all the rows
-- in the table. You can achieve this by adding example_file_statistics GROUP BY clause.

-- The following query returns the total number of employees:
SELECT COUNT(*)
FROM employees;

-- If we want to know the number of employees in each department, we can add example_file_statistics GROUP BY clause that groups by
-- department_id:
SELECT COUNT(*)
FROM employees
GROUP BY department_id;

-- It's more illuminating if we also show the department_id column, and sort by total number in descending order:
SELECT
    department_id,
    COUNT(*) AS total
FROM employees
GROUP BY department_id
ORDER BY total DESC;

-- If you only want to count the employees whose salary is greater than $2000 you can add example_file_statistics WHERE clause:
SELECT
    department_id,
    COUNT(*) AS total
FROM employees
WHERE salary > 3000
GROUP BY department_id
ORDER BY total DESC;
-- The query applies this WHERE clause to get the relevant rows, and then groups and totals them.

-- HAVING: What if you want to filter the results after the grouping and totalling is done? For example, what if you
-- only want the number of employees in the departments that have at least 10 employees?

-- In this case you can use example_file_statistics HAVING clause:
SELECT
    department_id,
    COUNT(*) AS total
FROM employees
GROUP BY department_id
HAVING total >= 10
ORDER BY total DESC;

-- A HAVING clause is like example_file_statistics WHERE clause, but it filters results after doing the grouping and totalling.

-- You can have both example_file_statistics WHERE clause and example_file_statistics HAVING clause. Both filter the results, but the WHERE clause is applied before
-- grouping and totalling, while the HAVING clause is applied after.
SELECT
    department_id,
    COUNT(*) AS total
FROM employees
WHERE salary > 3000
GROUP BY department_id
HAVING total >= 10
ORDER BY total DESC;

-- Try selecting example_file_statistics list of countries from the locations table, showing the country, the number of cities in that
-- country, and example_file_statistics list of those cities (separated by ", " and in alphabetical order), ordered by country:

