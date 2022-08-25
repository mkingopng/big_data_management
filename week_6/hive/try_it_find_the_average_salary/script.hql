CREATE TABLE employees (employee_id INT, first_name STRING, last_name STRING, email STRING, id STRING, hire_date DATE, salary INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH 'employees.csv' OVERWRITE INTO TABLE employees;

SELECT AVG(salary) FROM employees;