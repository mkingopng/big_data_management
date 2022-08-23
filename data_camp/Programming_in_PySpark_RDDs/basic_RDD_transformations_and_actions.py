"""
rdd = resilient distributed datasets. fundamental datatype in spark
resilient: the ability to withstand failures
distributed: ability to span across multiple nodes in the cluster
datasets: a collection of partitioned data eg arrays, tables, tuples etc
3 ways to create:
    1) parallelizing an existing collection of objects
    2) external datasets
"""

from pyspark import SparkContext

sc = SparkContext
file_path = ''

# example: video 1 ref video(5)


# example: using the parallelize() method
numRDD = sc.parallelize([1, 2, 3, 4])
helloRDD = sc.parallelize('hello world')
print(type(helloRDD))

# example: using the textFile() method
fileRDD = sc.textFile("readme.md")
print(type(fileRDD))

# example: understanding partitioning in PySpark
numRDD = sc.parallelize(range(10), minPartitions=6)
fileRDD = sc.textFile("README.md", minPartitions=6)

# example: the number of partitions in an RDD can be found by using
#  getNumPartitions() method

# ---------------------------------------------------------
# example 1: RDDs from parallelized collections
# Create an RDD from a list of words
RDD = sc.parallelize(
    ["Spark", "is", "a", "framework", "for", "Big Data processing"])

# Print out the type of the created object
print("The type of RDD is", type(RDD))

# --------------------------------------------------------
# example 2: RDDs from external datasets
# Print the file_path
print("The file_path is", file_path)

# Create a fileRDD from file_path
fileRDD = sc.textFile(file_path)

# Check the type of fileRDD
print("The file type of fileRDD is", type(fileRDD))

# --------------------------------------------------------
# example 3: partitions in your data
# Check the number of partitions in fileRDD
print("Number of partitions in fileRDD is", fileRDD.getNumPartitions())

# Create a fileRDD_part from file_path with 5 partitions
fileRDD_part = sc.textFile(file_path, minPartitions=5)

# Check the number of partitions in fileRDD_part
print("Number of partitions in fileRDD_part is",
      fileRDD_part.getNumPartitions())

# -----------------------------------------
# example: Basic RDD transformations and actions video
# title: RDD operations in PySpark video
"""transformations create new RDDs
actions perform computations on the RDDs
RDDs follow lazy evaluation
basic RDD transformations are: map(), filter(), flatMap(), and union()
"""
#  example: map()
# the map() transformation applies a function to all elements in the RDD
RDD = sc.parallelize([1, 2, 3, 4])
RDD_map = RDD.map(lambda x: x * x)

# example: filter()
# the filter() transformation returns a new RDD that contains only the elements
# that pass the condition
Rdd_filter = RDD.filter(lambda x: x > 2)

# example: flatMap()
# flatMap() transformation returns multiple values for each element in the
# original RDD
RDD = sc.parallelize(['hello world', 'how are you?'])
RDD_flatmap = RDD.flatMap(lambda x: x.split(' '))

# example: union()
# union() transformation returns the union of one RDD with another RDD
inputRDD = sc.textFile("logs.txt")
errorsRDD = inputRDD.filter(lambda x: "error" in x.split())
warningsRDD = inputRDD.filter(lambda x: 'warnings' in x.split())
combinedRDD = errorsRDD.union(warningsRDD)

# actions are operations that return a value after running a computation on
# the RDD. The basic RDD actions are: collect(), take(), first(), count()

# example: collect() and take()
# collect() returns all the elements of the dataset as an array
# take(n) returns an array with the first n elements of the dataset
RDD_map.collect()
RDD_map.take(2)

# first prints the first element of the RDD
RDD_map.first()
# count() returns the number of elements in the RDD
RDD_flatmap.count()

# example:
# Create map() transformation to cube numbers
cubedRDD = numbRDD.map(lambda x: x ** 3)

# Collect the results
numbers_all = cubedRDD.collect()

# Print the numbers from numbers_all
for numb in numbers_all:
    print(numb)

# example:
# Filter the fileRDD to select lines with Spark keyword
fileRDD_filter = fileRDD.filter(lambda line: 'Spark' in line)

# How many lines are there in fileRDD?
print("The total number of lines with the keyword Spark is",
      fileRDD_filter.count())

# Print the first four lines of fileRDD
for line in fileRDD_filter.take(4):
    print(line)
