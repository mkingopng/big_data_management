from pyspark.sql import SparkSession, Row
from pyspark import SparkContext, SparkConf

# create a spark context instance
sc = SparkContext('local', 'employeesTxt')

# load the text file and convert each line to a Row object.
text = sc.textFile("employees.txt")
parts = text.map(lambda l: l.split(","))
employees_txt = parts.map(
    lambda p: Row(
        employee_id=p[0],
        first_name=p[1],
        last_name=p[2],
        hire_date=p[5],
        salary=float(p[6])
    )
)

# use createDataFrame and createOrReplaceTempView to infer the schema, and register the DataFrame as a table.
spark = SparkSession.builder.master("local").appName("employees").getOrCreate()
schemaEmployees = spark.createDataFrame(employees_txt)
schemaEmployees.createOrReplaceTempView("employees")

# SQL can be run over DataFrames that have been registered as a table
results = spark.sql(
    "SELECT first_name,"
    "last_name, "
    "hire_date, "
    "salary "
    "FROM employees "
    "WHERE hire_date LIKE '2007-%' AND salary > 6000"
)

# show the results then close the spark context instance and spark session
results.show()
sc.stop()
spark.stop()
