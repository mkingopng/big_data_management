from pyspark.sql import SparkSession

#
spark = SparkSession.builder.master("local").appName("termrank").getOrCreate()

#
df = spark.read.text("file:///home/abcnews.txt")

#
df.selectExpr("split(value, ',')[0] as date", "split(value, ',')[1] as headline").createOrReplaceTempView("abcnews")

#
year_terms = spark.sql("SELECT SUBSTR(date,0,4) as year, term FROM abcnews lateral view EXPLODE(split(headline, ' ')) as term")

#
year_terms.createOrReplaceTempView("year_terms")

#
termcount = spark.sql("SELECT year, term, count(*) AS num FROM year_terms GROUP BY year, term")

#
ranked_res = termcount.orderBy(termcount.year, termcount.num.desc(), termcount.term)

#
ranked_res.write.format("csv").save("file:///home/output")
