# DataFrames in a Python shell

Let's see how to work with DataFrames in Spark. We'll start by working in a Python 
shell. And we'll work with a CSV file.

If you click on the panel on the right you will get a terminal connection to a 
server with Hadoop and YARN installed and running.

In your home directory on the server there is a CSV file called "employees.csv". To 
work with this file using Spark we need to put it into HDFS:

> $ hdfs dfs -mkdir -p /user/user
 
> $ hdfs dfs -put employees.csv

Now let's start a Python shell, with Spark loaded into Python for us:
> $ pyspark

# Creating a DataFrame

In addition to the `sc` object which we have used to create and work with RDDs, your 
Python shell also has an object `spark` which we will use to create and work with 
DataFrames.

First, we can create a DataFrame by loading the data in employees.csv, as follows:
> employees = spark.read.format("csv").option("header", "true").load("employees.csv")

Here we are using the `read` property of the `spark` object. We specify that the format 
of the file we want to read is csv, and that it has a header row, and that it is called 
"employees.csv". Spark assumes that it is our default working directory in HDFS, as 
it is. 

You now have an DataFrame called "employees" which contains the contents of the file 
"employees.csv". To see the number of items in the DataFrame you can use the `count()` 
action on the DataFrame:
> employees.count()

To see the first item of the DataFrame you can use the `first()` action:
> employees.first()

So far this is working just like an RDD. But now let's doing something new - use SQL 
statements to query the data.

# Using SQL

We first need to create a temporary table (a view). Let's call it "employees". We 
do so using the following command:
> employees.createOrReplaceTempView("employees")

Now we can run some queries to answer some questions. To do so we use the `sql()` 
method of the `spark` object.

What is the maximum salary of employees?
> spark.sql("SELECT MAX(int(salary)) FROM employees").show()

Note that we have used the `show()` method at the end. This tells Spark to show us 
the results.

What are the distinct salaries, and which employees have those salaries?
> spark.sql("SELECT salary, COLLECT_LIST(last_name) FROM employees GROUP BY salary").show()

Which employee have the highest salary?
> spark.sql("SELECT first_name, last_name, salary FROM employees WHERE salary = (SELECT MAX(int(salary)) FROM employees)").show()

Which employees were hired in 2007 and have a salary of more than $6,000?
> spark.sql("SELECT first_name, last_name, hire_date, salary FROM employees WHERE hire_date LIKE 