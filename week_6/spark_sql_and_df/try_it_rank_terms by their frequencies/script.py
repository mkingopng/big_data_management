from pyspark.sql import SparkSession

# start a spark session
spark = SparkSession.builder.master("local").appName("termrank").getOrCreate()

# read the file
df = spark.read.text("file:///home/abcnews.txt")

#
df.selectExpr("split(value, ',')[0] as date", "split(value, ',')[1] as headline").createOrReplaceTempView("abcnews")

# spark SQL query
year_terms = spark.sql("SELECT SUBSTR(date,0,4) as year, term FROM abcnews lateral view EXPLODE(split(headline, ' ')) as term")

# create a temporary view
year_terms.createOrReplaceTempView("year_terms")

# query the view
termcount = spark.sql("SELECT year, term, count(*) AS num FROM year_terms GROUP BY year, term")

#
ranked_res = termcount.orderBy(termcount.year, termcount.num.desc(), termcount.term)

# write the output to the directory
ranked_res.write.format("csv").save("file:///home/output")
