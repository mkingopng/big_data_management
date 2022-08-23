from pyspark import SparkContext

# create HDFS directory
# hdfs dfs -mkdir -p /user/user

# move txt files to it
# hdfs dfs -put abcnews.txt
# hdfs dfs -put stopwords.txt

# define the file paths
abc_news = 'file:///home/abcnews.txt'
stop_words = 'file:///home/stopwords.txt'
output = 'file:///home/output'

# create a spark context
sc = SparkContext()

# read the txt file
baseRDD = sc.textFile(abc_news)

# Split on commas
splitRDD = baseRDD.flatMap(lambda x: x.split(','))

# check
for word in splitRDD.take(10):
    print(word)

# split on spaces
second_split = splitRDD.flatMap(lambda x: x.split())

# Count the total number of words

# groupby(year)

# groupby(year) and sum(count)

# sort into top 3 per year with the format <>

# save to file

# close sc()

# show file

# run the program
# spark-submit rdd.py

# ------------------------------
from pyspark import SparkContext

abc_news = 'file:///home/abcnews.txt'

stop_words = 'file:///home/stopwords.txt'

output = 'file:///home/output'

sc = SparkContext()

baseRDD = sc.textFile(abc_news)

# the dates are left of the comma
dates = baseRDD.flatMap(lambda line: line.split(','))
words = baseRDD.flatMap(lambda line: line.split())

for date in dates.take(10):
    print(date)

for word in words.take(10):
    print((word, 1))

# def even(x): return x % 2 == 0
# def odd(x): return not even(x)

# the text is right of the comma
# textRDD = baseRDD.flatMap(lambda line: line.split(',')[1])
# for words in textRDD.take(10):
#     print(words)

# split the text on spaces
# splitRDD = text.flatMap(lambda text: text.split())


# Convert the words in lower case & remove stop words from the stop_words list
# splitRDD_no_stop = splitRDD.filter(lambda x: x.lower() not in stop_words)

# # Create a tuple of the word and 1
# splitRDD_no_stop_words = splitRDD_no_stop.map(lambda word: (word, 1))

# # Count of the number of occurrences of each word
# resultRDD = splitRDD_no_stop_words.reduceByKey(lambda x, y: x + y)

# save the output
# RDD.coalesce(1).saveAsTestFile('output')

# sc.stop()