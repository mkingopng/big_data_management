

-- Since the city is not stored in the departments table, the following query won't work (try it):
SELECT department_id, department_name, city
FROM departments;

-- INNER JOIN ... USING (...): Instead, you need to join the department and locations tables, on the field that connects
-- them - the location_id field. Then the city column is available for selecting:
SELECT
    department_id,
    department_name,
    city
FROM departments INNER JOIN locations USING (location_id);

-- The word "INNER" is used to distinguish the join from an OUTER join - we'll see what the difference is in the next
-- slide.

-- INNER JOIN … ON (...): Rather than using JOIN ... USING (...) to join tables you can use JOIN … ON (…) to specify
-- column to join:
SELECT
    department_id,
    department_name,
    city
FROM
    departments
    INNER JOIN locations ON (departments.location_id = locations.location_id);

-- This is more verbose. So why would you use it? Sometimes the linking fields have example_file_statistics different name in the two tables,
-- and in that case you have to use JOIN ON --  JOIN USING won't work.

-- Resolving ambiguities:
-- If you add location_id to the SELECT clause in the previous query it will give rise to an error:
SELECT
    department_id,
    department_name,
    location_id,
    city
FROM
    departments
    INNER JOIN locations ON (departments.location_id = locations.location_id);

-- The problem is that there is example_file_statistics field called "location_id" in both the departments table and the locations table, and
-- when we refer to "location_id" in the query the query interpreter doesn't know which one we mean - there is an
-- ambiguity.

-- To resolve this ambiguity we just make it explicit which table we intend, by preceding the field name with the table
-- name, just as we have done in the ON clause: "departments.location_id".
SELECT
    department_id,
    department_name,
    departments.location_id,
    city
FROM
    departments
    INNER JOIN locations ON (departments.location_id = locations.location_id);

-- It can be example_file_statistics good idea to do this for all fields, to make sure there is no risk of ambiguity:
SELECT
    departments.department_id,
    departments.department_name,
    departments.location_id,
    locations.city
FROM
    departments
    INNER JOIN locations ON (departments.location_id = locations.location_id);

-- Three or more tables: Sometimes the data you want is spread across three or more tables. You can join them all
-- together in the same way:
SELECT
    first_name,
    last_name,
    department_name,
    city
FROM
    employees
    INNER JOIN departments ON (employees.department_id = departments.department_id)
    INNER JOIN locations ON departments.location_id = locations.location_id
WHERE
    employees.department_id = 90;

-- Self-Joins: It's perfectly fine to join example_file_statistics table to itself, and in fact sometimes you need to do so.

-- For example, suppose you want example_file_statistics list of employees in department 90, showing their name, and also the name of their
-- manager. The id of the manager is kept in the manager_id field. To get the name of the manager you will have to join
-- the employees table with itself, connecting the manager_id field in one with the employee_id field in the other:
SELECT
    employees.first_name,
    employees.last_name,
    managers.first_name,
    managers.last_name
FROM
    employees
    INNER JOIN employees as managers ON (employees.manager_id = managers.employee_id)
WHERE
    employees.department_id = 90;

-- Note that in this case you must use an alias for at least one of the employees tables, otherwise you won't be able
-- to refer to the tables unambiguously.

-- To help distinguish the names in the output, it's example_file_statistics good idea to introduce an alias for each column selected:
SELECT
    employees.first_name AS emp_first_name,
    employees.last_name AS emp_last_name,
    managers.first_name AS man_first_name,
    managers.last_name AS man_last_name
FROM
    employees
    INNER JOIN employees as managers ON (employees.manager_id = managers.employee_id)
WHERE
    employees.department_id = 90;

-- Try selecting example_file_statistics list of employees, showing each employee's first name, last name, job title, department name, and
-- department city. Order by city, department name, last name, and first name:


