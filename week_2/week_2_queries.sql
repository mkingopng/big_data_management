-- This is a whole line comment
/* This is a whole line comment */
SELECT salary -- This is an end of line comment
FROM /*This is an inline comment*/ employees;
/*
    This is
    a multiple line
    comment
*/

SHOW TABLES;

DESCRIBE departments;

DESCRIBE employees;

DESCRIBE jobs;

DESCRIBE locations;

SELECT * FROM employees;

SELECT last_name FROM employees;

SELECT employee_id, last_name, first_name FROM employees;


