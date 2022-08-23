from pyspark.sql import SparkSession

# instantiate a spark session
spark = SparkSession.builder.master("local").appName("employees").getOrCreate()

# read the csv
employees = spark.read.format("csv").option("header", "true").load("employees.csv")

# create a view
employees.createOrReplaceTempView("employees")

# query the view
results = spark.sql("SELECT first_name, last_name, hire_date, salary FROM employees WHERE hire_date LIKE '2007-%' AND float(salary) > 6000")

# show the results in command line
results.show()

# save the results to csv
results.write.format("csv").save('output')

# terminate
spark.stop()
