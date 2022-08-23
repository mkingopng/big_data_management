import pyspark

# hdfs dfs -mkdir -p /user/user

# hdfs dfs -put employees.csv

# create a DataFrame by loading the data in employees.csv
employees = spark.read.format("csv").option("header", "true").load("employees.csv")

# the number of items in the DataFrame
employees.count()

# the first item of the DataFrame
employees.first()

# create a temporary table (a view)
employees.createOrReplaceTempView("employees")

# What is the maximum salary of employees?
spark.sql("SELECT MAX(int(salary)) FROM employees").show()

# What are the distinct salaries, and which employees have those salaries?
spark.sql("SELECT MAX(int(salary)) FROM employees").show()

# Which employee have the highest salary?
spark.sql("SELECT first_name, last_name, salary FROM employees WHERE salary = (SELECT MAX(int(salary)) FROM employees)").show()

# Which employees were hired in 2007 and have a salary of more than $6,000?
spark.sql("SELECT first_name, last_name, hire_date, salary FROM employees WHERE hire_date LIKE '2007-%' AND salary > 6000").show()

