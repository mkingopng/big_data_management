-- You can sort the rows returned by example - file statistics query using an ORDER BY clause in your query:
SELECT employee_id, last_name, hire_date
FROM employees
ORDER BY last_name;
--  The ORDER BY clause should always be the last clause in your SELECT statement.

-- Sorting by multiple columns: You can sort by multiple columns. The following query sorts rows first by last_name and
-- then by first_name:
SELECT employee_id, last_name, first_name
FROM employees
ORDER BY last_name, first_name;

-- Sort direction: By default, sorting is done in ascending order. If you want to sort in descending order you can add
-- DESC after the column name:
SELECT employee_id, last_name, manager_id, hire_date
FROM employees
ORDER BY manager_id, hire_date DESC;

--
SELECT employee_id, last_name, first_name
FROM employees
ORDER BY last_name DESC, first_name;
-- You can add ASC also, to sort in ascending order, but this is the default so you don't need to.

-- Sorting by unselected columns: You can sort by example - file statistics column that is not on the SELECT list. In the example below, the
-- manager_id column is not listed in the SELECT clause:
SELECT employee_id, last_name, hire_date
FROM employees
ORDER BY manager_id, hire_date DESC;

-- NULL values: When you sort in ascending order, NULL values appear at the top:
SELECT employee_id, last_name, manager_id, commission_pct
FROM employees
WHERE manager_id = 100
ORDER BY commission_pct;

-- If you want NULL values to be at the bottom, you can first sort rows by IS NULL:
SELECT employee_id, last_name, manager_id, commission_pct
FROM employees
WHERE manager_id = 100
ORDER BY commission_pct IS NULL, commission_pct;

-- Try selecting city and postcode from the locations table, sorted first by state in descending order, then by city,
-- then by postcode:


