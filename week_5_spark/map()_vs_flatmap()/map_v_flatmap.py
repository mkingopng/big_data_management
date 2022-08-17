from pyspark import SparkContext

# enter this into the command line
# pyspark

# this is not in the original code
sc = SparkContext('local', 'frequencies')

# we load the file into an RDD directly from your local file system
file = sc.textFile("file:///home/text.txt")
file.collect()

# we use map to operate the file.
file.map(lambda x: x.split(" ")).collect()

# we use flatmap to operate the file.
file.flatMap(lambda x: x.split(" ")).collect()

# From this example, you could understand why we use flatMap rather
# than map in the word count problem.
