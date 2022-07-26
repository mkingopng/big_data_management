-- Aggregate functions
-- There are special functions that you can use to get totals, called aggregate functions.

-- COUNT
-- To find the total number of rows in a table you can use COUNT(*):
SELECT
    COUNT(*)
FROM
    employees;

-- To find the total number of department_ids in the employees table you can use:
SELECT
    COUNT(department_id)
FROM
    employees;

-- Notice that this only returns 106. Why not 107, as for the first query? Because one of the department_ids is NULL,
-- and that doesn't get counted. You can verify there is one such row using the following query:
SELECT *
FROM employees
WHERE department_id IS NULL;

-- If you just want the total number of distinct department_ids in the employees table you can add the keyword DISTINCT:
SELECT COUNT(DISTINCT department_id)
FROM employees;

-- MIN, MAX, and AVG: To find the minimum, maximum, and average salaries in the employees table you can use:
SELECT
    MIN(salary),
    MAX(salary),
    AVG(salary)
FROM employees;

-- SUM: To find the sum of salaries in the employees table you can use:
SELECT SUM(salary)
FROM employees;

-- You can verify that AVG() gets the right results by doing the calculation from first principles:
SELECT
    AVG(salary),
    SUM(salary)/COUNT(salary)
FROM employees;

-- GROUP_CONCAT: Rather than counting or summing the values you can combine them into a string, using the GROUP_CONCAT
-- function:
SELECT
    GROUP_CONCAT(city)
FROM locations

-- By default, a comma is used as the separator. You can specify an alternative by using the SEPARATOR keyword:
SELECT
    GROUP_CONCAT(city SEPARATOR '; ')
FROM locations

-- You can also specify how you would like the items to be ordered, by adding ORDER BY (and DESC, if you want descending
-- order):
SELECT GROUP_CONCAT(city ORDER BY city DESC SEPARATOR '; ')
FROM locations;

-- Does it matter what order you use ORDER BY and SEPARATOR? Try for yourself:
SELECT GROUP_CONCAT(city SEPARATOR '; ' ORDER BY city DESC)
FROM locations;

-- Working with NULLs
-- Be careful when using aggregate functions on columns that contain NULL values. The AVG() function, for example,
-- ignores NULL values when calculating averages.

-- Here's an example where this matters. Each of the two queries below calculates the average commission paid to
-- employees, but they treat NULL values of commission_pct differently. The first ignores them, whereas the second
-- counts them as 0. Thus, the first query returns a higher average than the second. In a bit more detail: The first
-- query leaves NULL values of commission_pct as NULL. When salary is multiplied by NULL the result is NULL, and these
-- NULLs are ignored by the AVG() function. The second query converts NULL values of commission_pct to 0. When salary is
-- multiplied by 0 the result is 0, and these 0s are included in the AVG() function.

-- Leave NULL values of commission_pct as NULL
SELECT
    COUNT(*) AS total_rows,
    COUNT(salary * commission_pct) AS included_rows,
    AVG(salary * commission_pct) AS average
FROM employees;

-- Change NULL values of commission_pct into 0
SELECT
    COUNT(*) AS total_rows,
    COUNT(salary * IFNULL(commission_pct, 0)) AS included_rows,
    AVG(salary * IFNULL(commission_pct, 0)) AS average
FROM employees;

-- Try selecting the number of distinct cities in the locations table:



