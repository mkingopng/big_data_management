from pyspark.sql import SparkSession

#
spark = SparkSession.builder.master("local").appName("employees").getOrCreate()

#
employees = spark.read.format("csv").option("header", "true").load("employees.csv")

#
employees.createOrReplaceTempView("employees")

#
results = spark.sql("SELECT salary,  collect_list(last_name) as lat_names FROM employees GROUP BY salary")

# Or concat the list

# results = spark.sql("SELECT salary, concat_ws(',', collect_list(last_name)) as lat_names FROM employees GROUP BY salary")

results.show()
spark.stop()
