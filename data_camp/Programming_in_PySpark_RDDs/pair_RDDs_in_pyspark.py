"""

There are two common ways to create pair RDDs
    - from a list of key-value tuple
    - from a regular RDD
The first step is to get the data into key-value form for paired RDD
"""
from pyspark import SparkContext

sc = SparkContext

my_tuple = [('Sam', 23), ('Mary', 34), ('Peter', 25)]
pairRDD_tuple = sc.parallelize(my_tuple)

# here is an example of creating paired RDDs from regular RDDs
my_list = ['Sam 23', 'Mary 34', 'Peter 25']
regularRDD = sc.parallelize(my_list)
pairRDD = regularRDD.map(lambda s: (s.split(' ')[0], s.split(' ')[1]))

"""
all the regular transformations work on pair RDDs. We have to pass functions 
that operate on key value pairs rather than individual elements. Examples of
pair RDD transformations include:
    - reduceByKey(): combine values with the same key using a function. it runs 
    parallel operations for each key in the dataset
    - groupByKey(): group values with the same key in the pair RDD
    - sortByKey(): return an RDD sorted by the key in ascending or descending 
    order
    - join(): join two pair RDDs based on their key
"""
regularRDD = sc.parallelize([('Messi', 23), ('Ronaldo', 34),
                             ('Neymar', 22), ('Messi', 24)])
pairRDD_reducebykey = regularRDD.reduceByKey(lambda x, y: x + y)
pairRDD_reducebykey.collect()

# example: sortByKey()
pairRDD_reducebykey_rev = pairRDD_reducebykey.map(lambda x: (x[1], x[0]))
pairRDD_reducebykey_rev.sortByKey(ascending=False).collect()

# example: groupByKey()
airports = [('US', 'JFK'), ('UK', 'LHR'), ('FR', 'CDG'), ('US', 'SFO')]
regularRDD = sc.parallelize(airports)
pairRDD_group = regularRDD.groupByKey().collect()
for cont, air in pairRDD_group:
    print(cont, list(air))

# example: join() transformation
RDD1 = sc.parallelize([('Messi', 34), ('Ronaldo', 32), ('Neymar', 24)])
RDD2 = sc.parallelize([('Ronaldo, 80'), ('Neymar', 120), ('Messi', 100)])
RDD1.join(RDD2).collect()

# example 1: reduceByKey() and collect()
# Create PairRDD Rdd with key value pairs
Rdd = sc.parallelize([(1, 2), (3, 4), (3, 6), (4, 5)])

# Apply reduceByKey() operation on Rdd
Rdd_Reduced = Rdd.reduceByKey(lambda x, y: x + y)

# Iterate over the result and print the output
for num in Rdd_Reduced.collect():
    print("Key {} has {} Counts".format(num[0], num[1]))

# example 2: sortByKey() and collect()
# Sort the reduced RDD with the key by descending order
Rdd_Reduced_Sort = Rdd_Reduced.sortByKey(ascending=False)

# Iterate over the result and retrieve all the elements of the RDD
for num in Rdd_Reduced_Sort.collect():
  print("Key {} has {} Counts".format(num[0], num[1]))
