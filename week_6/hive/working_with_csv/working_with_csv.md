# Working with CSV
In the previous slides we were using Hive to query data in a text file. Now 
let's use Hive to query data a CSV file. 

Click the panel on the right. This will give you a terminal connection to a 
server that has Hadoop, YARN and Hive installed and running, and has a file 
called "employees.csv" in your home directory.

Run the following command to start a Hive shell:
> $ hive

# Create a table
Let's create a table into which we can load the CSV file. Here are the fields 
in the CSV file:

```
employee_id (integer)
first_name (string)
last_name (string)
email (string)
phone_number (string)
hire_date (date)
salary (integer)
```

Given this structure of the CSV file, we should create our table as follows:
> CREATE TABLE employees (employee_id INT, first_name STRING, last_name STRING, email STRING, phone_number STRING, hire_date DATE, salary INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' STORED AS TEXTFILE;

You can check that the table has been created by running the following command:
> SHOW TABLES;

You can check the structure of the table by running the following command:
> DESCRIBE employees;

# Load data
Now let's load the CSV file into the table:
> LOAD DATA LOCAL INPATH 'employees.csv' OVERWRITE INTO TABLE employees;

You can check that the data has been loaded by running the following command:
> SELECT * FROM employees;

# Run queries
Now let's run some HQL queries to answers questions about the data in the CSV 
file.

What is the maximum salary of employees?
> SELECT MAX(salary) FROM employees;

What are the distinct salaries, and which employees have those salaries?
> SELECT salary, COLLECT_LIST(last_name) FROM employees GROUP BY salary;

Note that Hive uses COLLECT_LIST rather than GROUP_CONCAT (which is what MySQL uses).

Which employees were hired in 2006 and have a salary of more than $5,000?
> SELECT first_name, last_name, hire_date, salary FROM employees WHERE hire_date LIKE '2006-%' AND salary > 5000;

 