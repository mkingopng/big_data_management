from pyspark import SparkContext

# create HDFS directory
# $ hdfs dfs -mkdir -p /user/user

# move txt files to it
# $ hdfs dfs -put orders.csv

orders_path = 'orders.csv'

sc = SparkContext()

# create an RDD from csv file using textFile() method
orders_file = sc.textFile(orders_path).map(lambda line: line.strip().split(','))

# map() the order pairs, with orderDate as key and quantity as value
orders_pairs = orders_file.map(lambda x: (x[0], x[5].asint()))

# check
for pairs in orders_pairs.take(10):
    print(pairs)
