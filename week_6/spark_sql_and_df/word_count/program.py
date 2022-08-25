from pyspark.sql import SparkSession
from pyspark.sql.functions import *

#
spark = SparkSession.builder.master("local").appName("termrank").getOrCreate()

#
spark.read().text("file_name")

#
fileDF = spark.read.text("file:///home/text.txt")

#
fileDF = fileDF.filter(fileDF.value != "")

#
fileDF.show()

#
wordDF = fileDF.select(explode(split(lower(fileDF.value), ' ')).alias("word"))

#
countDF = wordDF.groupBy("word").count()

#
sortedDF = countDF.orderBy("word")
# or
# sortedDF = countDF.orderBy(countDF.word)

#
sortedDF.show()

#
sortedDF.select(concat(col("word"), lit(':'), col("count")).cast("string")).write.format("text").mode("append").save("file:///home/output")

#
sortedDF.write().text("sortedDF")
