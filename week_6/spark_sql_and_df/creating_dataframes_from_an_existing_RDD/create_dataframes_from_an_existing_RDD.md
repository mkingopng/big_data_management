# Create DataFrames from an existing RDD

Now let's see how to create DataFrames from an existing RDD.

If you click on the panel on the right you will get a terminal connection 
to a server with Hadoop and YARN installed and running. In your home 
directory on the server, there is a text file called "employees.txt".  
And there is also a Python program called "program.py".

The task is to find the employees who were hired in 2007 and have a salary 
of more than $6,000.

We first load the text file and convert each line to a Row object.

> sc = SparkContext('local', 'employeesTxt') 

> text = sc.textFile("employees.txt") 

> parts = text.map(lambda l: l.split(",")) 

> employees_txt = parts.map(lambda p: Row(employee_id=p[0],first_name=p[1],last_name=p[2],hire_date=p[5],salary=float(p[6])))

Next, we use `createDataFrame` and `createOrReplaceTempView` to infer the 
schema, and register the DataFrame as a table.

> spark = SparkSession.builder.master("local").appName("employees").getOrCreate()

> schemaEmployees = spark.createDataFrame(employees_txt)

> schemaEmployees.createOrReplaceTempView("employees")


At last, SQL can be run over DataFrames that have been registered as a table.

> results = spark.sql("SELECT first_name, last_name, hire_date, salary FROM employees WHERE hire_date LIKE '2007-%' AND salary > 6000")


To work with the text file using Spark we need to put it into HDFS:

> $ hdfs dfs -mkdir -p /user/user

> $ hdfs dfs -put employees.txt

Now we can submit the Python program to Spark:

> $ spark-submit program.py

You should see Spark begin to execute and produce the output.