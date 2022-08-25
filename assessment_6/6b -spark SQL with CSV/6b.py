from pyspark.sql import SparkSession, Row

#
spark = SparkSession.builder.master("local").appName("orders").getOrCreate()

#
orders = spark.read.format("csv").option("header", "true").load("dbfs:/FileStore/shared_uploads/michaelkennethkingston@gmail.com/orders.csv")

#
orders.createOrReplaceTempView("orders")

#
results = spark.sql("SELECT salary,  collect_list(last_name) as lat_names FROM employees GROUP BY salary")

#
results.show()

#
spark.stop()
