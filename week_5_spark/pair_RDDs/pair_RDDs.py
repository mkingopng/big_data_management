from pyspark import SparkContext

# enter this into the command line
# pyspark

# this is not in the original code
sc = SparkContext('local', 'frequencies')

# we want to create a regular RDD and turn it into a pair RDD
lines = sc.parallelize(["hello world", "this is a python program", "to create a pair RDD", "in spark"])

# returns a list/RDD of the strings above
lines.collect()

# if we want to create a pair RDD, in which the key is the first term of the string, and the value is the string itself
pairRDD = lines.map(lambda x: (x.split(" ")[0], x))

# check the new pair RDD
pairRDD.collect()

# keep only the lines whose first term containing less than three characters
pairRDD.filter(lambda x: len(x[0]) < 3).collect()

# create a pair RDD from a list
rdd = sc.parallelize([(1, 2), (3, 4), (3, 6)])

# check
rdd.collect()

# todo: check each operation below

# Operation: reduceByKey(func). Purpose: Combine values with the same key.
rdd.reduceByKey(lambda x, y: x + y)
rdd.reduceByKey(lambda x, y: x + y).collect()

# Operation: groupByKey(). Purpose: Group values with the same key. Example Command:
rdd.groupByKey()
rdd.groupByKey().collect()

# Operation: mapValues(func). Purpose: Apply a function to each value of a pair RDD without changing the key.
rdd.mapValues(lambda x: x+1)
rdd.mapValues(lambda x: x+1).collect()

# Operation: keys(). Purpose: Return an RDD of just the keys.
rdd.keys()
rdd.keys().collect()

# Operation: values(). Purpose: Return an RDD of just the values.
rdd.values()
rdd.values().collect()

# Operation: sortByKey(). Purpose: Return an RDD sorted by the key.
rdd.sortByKey()
rdd.sortByKey().collect()

# Operation: flatMapValues(func). Purpose: Apply a function that returns an iterator to
# each value of a pair RDD, and for each element returned, produce a key/value entry
# with the old key.
rdd.flatMapValues(lambda x: list(range(x, 6)))
rdd.flatMapValues(lambda x: list(range(x, 6))).collect()

# create another pair RDD, and practice some transformation operations over two pair RDDs
other = sc.parallelize([(3, 9)])
other.collect()

# Operation: subtractByKey. Purpose: Remove elements with a key present in the other RDD.
rdd.subtractByKey(other)
rdd.subtractByKey(other).collect()

# Operation: join. Purpose: Perform an inner join between two RDDs.
rdd.join(other)
rdd.join(other).collect()

# Operation: cogroup. Purpose: Group data from both RDDs sharing the same key.
rdd.cogroup(other)
rdd.cogroup(other).collect()

# todo: actions available on Pair RDDs

# Operation: countByKey(). Purpose: Count the number of elements for each key.
rdd.countByKey()

# Operation: collectAsMap(). Purpose: Collect the result as a map to provide easy lookup.
rdd.collectAsMap()
# Warning: this doesn't return a multimap. So if you have multiple values to the same key,
# only one value per key is preserved in the map returned.

# Operation: lookup(key). Purpose: Return all values associated with the provided key
rdd.lookup(3)
