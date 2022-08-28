import pyspark
from pyspark import SparkContext

# hdfs dfs -mkdir -p /user/user
# hdfs dfs -put text.txt
# pyspark

"""Python is now running with a SparkContext object sc created for you"""

# create an RDD:
text = sc.textFile("text.txt")

# To see the number of items in the RDD
text.count()

# To see the first item of the RDD
text.first()

# To see the first three items of the RDD
text.take(3)

# To see the contents of the RDD
text.collect()

# To see the lines that contain "war" you first filter the RDD, then collect it
text.filter(lambda line: "war" in line).collect()

# You can use the map() function to map each line of the file to the number of words the line contains.
word_nums = text.map(lambda line: len(line.split()))

# You can view the items in word_nums using collect():
word_nums.collect()

# To find the largest number of words in a line we can apply reduce() to word_nums
word_nums.reduce(lambda result, value: max(result, value))

# You can cache the data in memory:
word_nums.cache()

# create an RDD containing the words in the file. Apply the flatMap():
words = text.flatMap(lambda line: line.split())

# get the total number of words using count()
words.count()

# get the number of distinct words by first transforming words using distinct()
words.distinct().count()

# use map() to transform words into a new RDD that contains each of the words paired with a 1:
pairs = words.map(lambda word: (word, 1))

# Next, transform this RDD into a new RDD that contains the word frequencies:
frequencies = pairs.reduceByKey(lambda total, value: total + value)

# Finally, show the results:
frequencies.collect()

# You could also combine these commands into a single command:
text.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda total, value: total + value).collect()

# If at any stage you would like to save an RDD, do so by using saveAsTextFile(), and providing a path for the file:
frequencies.saveAsTextFile("results")

# First, you need to quit the Python shell
quit()

# Now you can check for the file in HDFS. You could use the following command:
# hdfs dfs -ls results
