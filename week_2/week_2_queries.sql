-- This is example_file_statistics whole line comment
/* This is example_file_statistics whole line comment */
SELECT salary -- This is an end of line comment
FROM /*This is an inline comment*/ employees;
/*
    This is
    example_file_statistics multiple line
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


