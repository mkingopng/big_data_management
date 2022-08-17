from pyspark import SparkContext


sc = SparkContext('local', 'frequencies')

text = sc.textFile("text.txt")

frequencies = text.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda total, value : total + value)

frequencies.saveAsTextFile("results")

sc.stop()
