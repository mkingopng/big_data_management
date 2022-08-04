# Pair RDDs
The items in an RDD can be of any type, but one type are especially important and useful: <key, value> pairs. When the 
items in an RDD are <key, value> pairs then the RDD is said to be a "pair RDD". This slide covers how to work with RDDs 
of key/value pairs. Key/value RDDs are commonly used to perform aggregations, and often we will do some initial ETL 
(extract, transform, and load) to get our data into a key/value format. Key/value RDDs expose new operations (e.g., 
counting up reviews for each product, grouping together data with the same key, and grouping together two different RDDs).

## Creating Pair RDDs
Normally, we have a regular RDD that we want to turn into a pair RDD. We can do this by running a map() function that 
returns key/value pairs. Open pyspark shell, and let's see an example as below.

`lines = sc.parallelize(["hello world", "this is a python program", "to create a pair RDD", "in spark"])`

`lines.collect()`

We can see that an RDD containing four strings have been created. Next, if we want to create a pair RDD, in which the 
key is the first term of the string, and the value is the string itself, we can do like:

`pairRDD = lines.map(lambda x: (x.split(" ")[0], x))`

You can try to check what are stored in the created pair RDD.

If you want to keep only the lines whose first term containing less than three characters, you can do:

`pairRDD.filter(lambda x: len(x[0])<3).collect()`

## Transformations on Pair RDDs
Pair RDDs are allowed to use all the transformations available to standard RDDs. Since pair RDDs contain tuples, we 
need to pass functions that operate on tuples rather than on individual elements.

Let's first create an pair RDD from the list 

[(1, 2), (3, 4), (3, 6)].

`rdd = sc.parallelize([(1, 2), (3, 4), (3, 6)])`

Next, try each operation as below to see the results and understand what the operation can do (you can use collect() 
to see the result of each operation, like rdd.keys().collect()).
- **Operation**: reduceByKey(func). Purpose: Combine values with the same key. Example Command: rdd.reduceByKey(lambda x, y: x + y)
- **Operation**: groupByKey(). Purpose: Group values with the same key. Example Command: rdd.groupByKey()
- **Operation**: mapValues(func). Purpose: Apply a function to each value of a pair RDD without changing the key. Example Command: rdd.mapValues(lambda x: x+1)
- **Operation**: keys(). Purpose: Return an RDD of just the keys. Example Command: rdd.keys()
- **Operation**: values(). Purpose: Return an RDD of just the values. Example Command: rdd.values()
- **Operation**: sortByKey(). Purpose: Return an RDD sorted by the key. Example Command: rdd.sortByKey()
- **Operation**: flatMapValues(func). Purpose: Apply a function that returns an iterator to each value of a pair RDD, and for each element returned, produce a key/value entry with the old key. Often used for
- **tokenization**. Example Command: rdd.flatMapValues(lambda x: list(range (x, 6)))

Next, let's create another pair RDD, and practice some transformation operations over two pair RDDs.

`other = sc.parallelize([(3, 9)])`

- **Operation**: subtractByKey. Purpose: Remove elements with a key present in the other RDD. Example Command: rdd.subtractByKey(other)
- **Operation**: join. Purpose: Perform an inner join between two RDDs. Example Command: rdd.join(other)
- **Operation**: cogroup. Purpose: Group data from both RDDs sharing the same key. Example Command: rdd.cogroup(other)

# Actions Available on Pair RDDs
As with the transformations, all of the traditional actions available on the base RDD are also available on pair RDDs. 
Some additional actions are available on pair RDDs to take advantage of the key/value nature of the data. 

Let's still use the previous RDD [(1, 2), (3, 4), (3, 6)], and practice some action operations over this RDD.
- **Operation**: countByKey(). Purpose: Count the number of elements for each key. Example Command: rdd.countByKey()
- **Operation**: collectAsMap(). Purpose: Collect the result as a map to provide easy lookup. Example Command: rdd.collectAsMap() (Warning: this doesn't return a multimap. So if you have multiple values to the same key, only one value per key is preserved in the map returned.)
- **Operation**: lookup(key). Purpose: Return all values associated with the provided key. Example Command: rdd.lookup(3)

