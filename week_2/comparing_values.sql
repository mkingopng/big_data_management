-- Comparing values

-- The following query selects employees who were hired on or after 8th March 2008:
SELECT
    employee_id,
    last_name,
    first_name,
    hire_date
FROM employees
WHERE hire_date >= '2008-03-08';

-- The following query selects departments whose location id is not 1700:
SELECT
    department_id,
    department_name,
    location_id
FROM departments
WHERE location_id <> 1700;

-- The following query selects employees whose department id is NULL:
SELECT
    employee_id,
    department_id
FROM employees
WHERE department_id IS NULL;

-- Adding NOT: You can filter for records that do not satisfy a certain condition by adding the NOT operator to the
-- condition. For example, to find employees whose department id is not 40 or 60 you could use:
SELECT employee_id, last_name, first_name, department_id
FROM employees
WHERE department_id NOT IN (40, 60);

-- Combining with AND and OR: You can filter for records that satisfy both of two conditions by using the AND operator.
-- To find employees whose salary is greater than $10,000 and less than $11,000 you could use:
SELECT
    employee_id,
    last_name,
    first_name,
    salary
FROM employees
WHERE salary > 10000 AND salary < 11000;

-- To find employees whose salary is at least $10,000 and no more than $11,000 you could use:
SELECT employee_id, last_name, first_name, salary
FROM employees
WHERE salary >= 10000 AND salary <= 11000;

-- To find employees whose id starts with 1, has any number in the middle, and ends with 9, and who was hired in the
-- year 2008, you could use:
SELECT
    employee_id,
    last_name,
    first_name,
    hire_date
FROM employees
WHERE employee_id LIKE '1_9' AND hire_date LIKE '2008-%';

-- You can filter for records that satisfy either of two conditions (or both) by using the OR operator.
-- To find employees whose last name starts with 'A' or 'B' you could use:
SELECT
    employee_id,
    last_name,
    first_name
FROM employees
WHERE last_name LIKE 'A%' OR last_name LIKE 'B%';

-- Beware of ambiguity
-- When you use an expression that contains two or more operators then it is a good idea to use parentheses to make it
-- clear how you intend them to be grouped. For example:
SELECT
    employee_id,
    last_name,
    first_name
FROM employees
WHERE (last_name LIKE 'A%' AND salary > 10000) OR last_name LIKE 'B%';

-- Comparing strings: When a comparison is done between two strings, the values are compared using ASCII codes. ASCII
-- stands for American Standard Code for Information Interchange. ASCII codes represent a number that computer or
-- software can translate. For example, the ASCII for character 1 is 49 (decimal).
SELECT
    location_id,
    postcode,
    country
FROM locations
WHERE postcode = 'YSW 9T2';

SELECT
    location_id,
    postcode,
    country
FROM locations
WHERE postcode > '9';

-- As you can see, 'M5V 2L7', 'YSW 9T2', and 'OX9 9ZB' are among the selected records. This is because the ASCII decimal
-- value for the number nine is 57 and, as an example, the ASCII decimal value for the letter 'Y' is 89. Since 89 is
-- greater than 57, these values are among the selected records.

-- BETWEEN ... AND ... operator: To select values in a certain range you can use a combination of operators as follows:
SELECT employee_id, last_name, first_name
FROM employees
WHERE last_name >= 'King' AND last_name <= 'Lee';

-- Alternatively, you can use the BETWEEN ... AND ... operator:
SELECT employee_id, last_name, first_name
FROM employees
WHERE last_name BETWEEN 'King' AND 'Lee';

-- You must specify the lower limit first - the following query returns no results:
SELECT employee_id, last_name, first_name
FROM employees
WHERE last_name BETWEEN 'Lee' AND 'King';

-- Try selecting all employees whose last name starts with 'A' or 'B' and whose salary is between $5000 and $10,000
-- (inclusive), showing each employee's last name and salary, ordered by last name ascending then salary descending:

