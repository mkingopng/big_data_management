from pyspark import SparkContext, SparkConf

sc = SparkContext()

textfile = sc.textFile('abcnews.txt')

words = textfile.flatMap(lambda line: line.split(' '))

pairs = words.map(lambda word: (word, 1))

count = pairs.reduceByKey(lambda a, b: a + b)

count.collect()

# spark-submit word_count.py
