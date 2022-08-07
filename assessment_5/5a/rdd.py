from pyspark import SparkContext, SparkConf

input_path = 'file:///home/abcnews.txt'

output_path = 'file:///home/output'

sc = SparkContext()

textfile = sc.textFile(input_path)

# get terms that have been used and filter by...
dates = textfile.map(lambda line: line.split(',')[0])

text = textfile.map(lambda line: line.split(',')[1])

terms = text.map(lambda text: text.split(' '))

# map() and reduceByKey() to count the number of times each term has been used
count = terms.map(lambda x: (int(x[1])).reduceByKey(lambda a, b: a + b)).filter(lambda x: x[1] > '3')

# sort the top-3 terms first by their article frequencies and then by the terms in alphabetical order
result = count.sortByKey(False).map(lambda x: x[0])

#
result.saveAsTextFile(output_path)

sc.stop()

# ----------

# spark-submit rdd.py

# ----------------------------------



# initially the key is the term, and the value is 1

# then group by date

# final key is date and values are top 3 terms for that date
