from pyspark import SparkContext, SparkConf

sc = SparkContext('local', 'longest')
text = sc.textFile("text.txt")
longest = text.flatMap(lambda line: line.split()).map(lambda word: len(word)).reduce(lambda total, value: max(total, value))
print("The longest word is", longest, "characters long")
sc.stop()
