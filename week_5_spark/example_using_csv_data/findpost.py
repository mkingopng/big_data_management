from pyspark import SparkContext, SparkConf

input_path = "file:///home/Votes.csv"
output_path = "file:///home/output"

sc = SparkContext('local', 'posts_favor')

textfile = sc.textFile(input_path)

# get posts that have been favored by users
posts = textfile.map(lambda line: line.split(',')).filter(lambda x: x[2] == '5')

# For each post, map() and reduceByKey() are used to count the number of users who have favored it.
# In this data set, each user can only favor a post once. The filter() operation keeps posts that
# have been favored by more than 5 users.
count = posts.map(lambda x: (int(x[1]), 1)).reduceByKey(lambda a, b: a + b).filter(lambda x: x[1] > 3)

# In count, PostIds have already been transformed to integers. So we can use sortByKey() to do
# the sorting, and then the map() operation throws away the count of users.
result = count.sortByKey(False).map(lambda x: x[0])

result.saveAsTextFile(output_path)
sc.stop()

# create default directory in hadoop
# hdfs dfs -mkdir -p /user/user

# copy the txt file to it
# hdfs dfs -put text.txt

# spark-submit findpost.py
