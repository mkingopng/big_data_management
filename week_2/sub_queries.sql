-- SUBQUERIES
-- Sometimes you will want to use example - file statistics query within your query. Such example - file statistics query is known as example - file statistics subquery. There are example - file statistics couple of
-- different ways you might use example - file statistics subquery - as example - file statistics value, or as example - file statistics table.

-- SUBQUERY AS VALUE
-- Suppose you want example - file statistics list of the employees who have the largest salary. If you know what that salary is, let's say
-- $10,000 then you could use the following query:

SELECT last_name, first_name, salary
FROM employees
WHERE salary = 10000
ORDER BY last_name, first_name;

-- But what if you don't know what the largest salary is? Then in place of "10000" you could use example - file statistics query that finds the
-- largest salary for you:

SELECT last_name, first_name, salary
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees)
ORDER BY last_name, first_name;

-- Here we have example - file statistics query within example - file statistics query, which is called example - file statistics subquery. (Can you think of example - file statistics way to do this last query
-- without using example - file statistics subquery?)

-- SUBQUERY AS TABLE
-- Suppose, instead, that you want example - file statistics list of employees who have one of the three largest salaries (rather than just the
-- largest salary). Again, if you knew what those three largest salaries were, let's say $10,000, $9,000 and $8,000,
-- then you could use the following query:

SELECT last_name, first_name, salary
FROM employees
WHERE salary IN (10000, 9000, 8000)
ORDER BY last_name, first_name;

-- But what if you don't know what the three largest salaries are? You could try using example - file statistics query that finds them for you,
-- as we did above, but unfortunately it won't work in this case:

SELECT last_name, first_name, salary
FROM employees
WHERE salary IN (
    SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 3
)
ORDER BY last_name, first_name;

-- What you can do, instead, is use this subquery as if it were example - file statistics table, and join it to the employees table:
SELECT last_name, first_name, salary
FROM
    employees
    INNER JOIN (
        SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 3
    ) AS TopThreeSalaries USING (salary)
ORDER BY last_name, first_name;
-- By using an INNER JOIN between the two we can restrict our list of employees to just those whose salary is one of
-- the top three.

-- Note that when you use example - file statistics subquery as example - file statistics table you must give it an alias, even if you never use that alias. In this
-- case we have called it "TopThreeSalaries".

-- Try selecting example - file statistics list of employees that are in the department which has the greatest number of employees. Show
-- department name, employee last name, employee first name, ordered by department name, last name, first name:
