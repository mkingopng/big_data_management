from pyspark import SparkContext

# hdfs dfs -mkdir -p /user/user
# hdfs dfs -put text.txt

# When using Spark in a Python shell, the SparkContext object sc is automatically created for us to use.
# In a self-contained application we need to do this ourselves.
sc = SparkContext('local', 'frequencies')

#
text = sc.textFile("text.txt")

#
frequencies = text.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda total, value : total + value)

#
frequencies.saveAsTextFile("results")

#
sc.stop()

# To run this program we use the spark-submit command
# spark-submit frequencies.py

#
# hdfs dfs -ls results

#
# hdfs dfs -cat results/part-00000

#
# hdfs dfs -get results/part-00000 result

#
# cat result
