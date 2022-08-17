from pyspark import SparkContext, SparkConf

# create default directory in hadoop
# hdfs dfs -mkdir -p /user/user

# copy the txt file to it
# hdfs dfs -put text.txt

# create the spark context
sc = SparkContext('local', 'longest')

#
text = sc.textFile("text.txt")

#
longest = text.flatMap(lambda line: line.split()).map(lambda word: len(word)).reduce(lambda total, value: max(total, value))

#
print("The longest word is", longest, "characters long")

#
sc.stop()

# run the program from the shell
# spark-submit longest.py
