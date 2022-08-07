-- You can combine columns by concatenating them, using the CONCAT() function (some versions of SQL allow you to use +
-- or ||):
SELECT CONCAT(first_name, last_name)
FROM employees;

-- You can concatenate as many columns as you like, and you can add literal values too:
SELECT CONCAT("Full name: ", first_name, " ", last_name)
FROM employees;

-- When using numeric literals you should not use quotes. You can use single quotes inside double quotes, and double
-- quotes inside single quotes:
SELECT CONCAT(first_name, "'s last name is ", '"', last_name, '"')
FROM employees;

-- Performing calculations: For the basic arithmetic operations of addition, subtraction, multiplication and division,
-- use +, -, * and /:
SELECT
    last_name,
    salary,
    salary * 0.10 AS "Increase",
    salary + (salary * 0.10) AS "New Salary"
FROM employees;

-- When working with NULL values there are some things to be aware of.
-- Any number multiplied by NULL is NULL
SELECT 10 * NULL, NULL * (34 + 123);

-- You can use IFNULL to replace NULL values with 0:
SELECT IFNULL(10, 0), IFNULL(NULL, 0);

-- Now you can get zero instead of NULL:
SELECT 10 * IFNULL(NULL, 0);

-- Try selecting employees, showing their "reverse name" (e.g. "Pitt, Brad") and total salary once commission is
-- included, sorted by reverse name:
SELECT *
FROM employees;

