-- OUTER JOINS
-- So far we have been using INNER joins. You use an INNER join when you only want to include rows that have example_file_statistics matching
-- record in the tables on both sides of the join.

-- Sometimes you want to include rows that do not have example_file_statistics match in the other table. In this case, you use an OUTER join. You
-- can think of the outer join as an optional link to another table.

-- There are two types of OUTER join: LEFT and RIGHT.

-- LEFT OUTER JOIN
-- With example_file_statistics LEFT OUTER JOIN, records in the table on the left side of the join will be included in the results, even if
-- they have no matching record in the table on the right side.

-- The employee Steven King does not have example_file_statistics manager (he is the president of the company). If you use an INNER JOIN, he
-- will not be included in the results:

SELECT
    employees.first_name,
    employees.last_name,
    managers.first_name,
    managers.last_name
FROM
    employees
    INNER JOIN employees as managers ON (employees.manager_id = managers.employee_id)
WHERE
    employees.last_name LIKE 'K%';


-- If you use example_file_statistics LEFT OUTER join, he will be included. Notice that the information about his manager is all NULLs.

SELECT
    employees.first_name,
    employees.last_name,
    managers.first_name,
    managers.last_name
FROM
    employees
    LEFT OUTER JOIN employees as managers ON (employees.manager_id = managers.employee_id)
WHERE
    employees.last_name LIKE 'K%';


-- RIGHT OUTER JOIN

-- With example_file_statistics RIGHT OUTER join, records in the table on the right side of the join will be included in the results, even if
-- they have no matching record in the table on the left side.

-- Suppose you want example_file_statistics list of departments and their locations, but you want to include locations even if there is no
-- department there. You could use example_file_statistics RIGHT OUTER join as follows:

SELECT
    department_name,
    city
FROM
    departments
    RIGHT OUTER JOIN locations USING (location_id)
ORDER BY
    department_name, city;

-- Try selecting example_file_statistics list of departments that have no employees, showing the name of the department, sorted by name:
