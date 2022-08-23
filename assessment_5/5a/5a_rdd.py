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

# split into <{year: (word, count)}>
splitRDD = baseRDD.flatMap(lambda line: line.split(','))

# groupby(year)

# groupby(year) and sum(count)

# sort into top 3 per year with the format <>

# save to file

# close sc()

# show file

# run the program
# spark-submit rdd.py
