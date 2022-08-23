"""
rdd = resilient distributed datasets. fundamental datatype in spark
resilient: the ability to withstand failures
distributed: ability to span across multiple nodes in the cluster
datasets: a collection of partitioned data eg arrays, tables, tuples etc

3 ways to create an RDD:
    1) parallelizing an existing collection of objects
    2) external datasets
    3)
"""
from pyspark import SparkContext

sc = SparkContext
file_path = ''

numRDD = sc.parallelize([1, 2, 3, 4])
helloRDD = sc.parallelize('hello world')
print(type(helloRDD))
print(type(helloRDD))

fileRDD = sc.textFile("readme.md")
print(type(fileRDD))


# example 1: RDDs from parallelized collections
# Create an RDD from a list of words
RDD = sc.parallelize(["Spark", "is", "a", "framework",
                      "for", "Big Data processing"])

# Print out the type of the created object
print("The type of RDD is", type(RDD))

# example 2: RDDs from external datasets
# Print the file_path
print("The file_path is", file_path)

# Create a fileRDD from file_path
fileRDD = sc.textFile(file_path)

# Check the type of fileRDD
print("The file type of fileRDD is", type(fileRDD))

# example 3: partitions in your data
# Check the number of partitions in fileRDD
print("Number of partitions in fileRDD is", fileRDD.getNumPartitions())

# Create a fileRDD_part from file_path with 5 partitions
fileRDD_part = sc.textFile(file_path, minPartitions=5)

# Check the number of partitions in fileRDD_part
print("Number of partitions in fileRDD_part is", fileRDD_part.getNumPartitions())
