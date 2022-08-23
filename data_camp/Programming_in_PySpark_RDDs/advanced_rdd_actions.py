"""
advanced RDD actions

    - reduce(): is used for aggregating the elements of a regular RDD. the
    function should be cumulative (changing the order of the operands does not
    change the result) and associative, so that it can be computed correctly in
    parallel

    - saveAsTextFile(): saves the RDD into a text file inside a directory, by
    default with each partition as a separate file. you can save it to a single
    text file by using the coalesce() method

There are also actions for pair RDDs. pair RDDs also leverage the value of the
key value data structure in pyspark

    - countByKey(): only available for type (K, V). counts the number of
    elements for each key

    - collectAsMap(): returns the key-value pairs in the RDD as a dictionary
"""
from pyspark import SparkContext

sc = SparkContext
file_path = ''
stop_words = ''

# example: of reduce() action
x = [1, 2, 3, 4]
RDD = sc.parallelize(x)
RDD.reduce(lambda x, y: x + y)

# example: saveAsTestFile() and coalesce()
RDD.saveAsTestFile('tempFile')
RDD.coalesce(1).saveAsTestFile('tempFile')

# example: countByKey() on a simple list
rdd = sc.parallelize([('a', 1), ('b', 1), ('a', 1)])
for key, val in rdd.countByKey().items:
    print(key, val)

# example: collectAsMap()
sc.parallelize([(1, 2), (3, 4)]).collectAsMap()

# Count the unique keys
total = Rdd.countByKey()

# What is the type of total?
print("The type of total is", type(total))

# Iterate over the total and print the output
for k, v in total.items():
    print("key", k, "has", v, "counts")

# Create a baseRDD from the file path
baseRDD = sc.textFile(file_path)

# Split the lines of baseRDD into words
splitRDD = baseRDD.flatMap(lambda x: x.split())

# Count the total number of words
print("Total number of words in splitRDD:", splitRDD.count())

# Convert the words in lower case and remove stop words from the stop_words
# curated list
splitRDD_no_stop = splitRDD.filter(lambda x: x.lower() not in stop_words)

# Create a tuple of the word and 1
splitRDD_no_stop_words = splitRDD_no_stop.map(lambda w: (w, 1))

# Count of the number of occurrences of each word
resultRDD = splitRDD_no_stop_words.reduceByKey(lambda x, y: x + y)

# Display the first 10 words and their frequencies from the input RDD
for word in resultRDD.take(10):
    print(word)

# Swap the keys and values from the input RDD
resultRDD_swap = resultRDD.map(lambda x: (x[1], x[0]))

# Sort the keys in descending order
resultRDD_swap_sort = resultRDD_swap.sortByKey(ascending=False)

# Show the top 10 most frequent words and their frequencies from the sorted RDD
for word in resultRDD_swap_sort.take(10):
    print("{},{}".format(word[1], word[0]))

# example 1: countByKeys
# Count the unique keys
total = Rdd.countByKey()

# What is the type of total?
print("The type of total is", type(total))

# Iterate over the total and print the output
for k, v in total.items():
    print("key", k, "has", v, "counts")

# example 2: create a base RDD and transform it
# Create a baseRDD from the file path
baseRDD = sc.textFile(file_path)

# Split the lines of baseRDD into words
splitRDD = baseRDD.flatMap(lambda x: x.split())

# Count the total number of words
print("Total number of words in splitRDD:", splitRDD.count())

# example 3: remove stop_words and reduce the dataset
# Convert the words in lower case and remove stop words from the stop_words
# curated list
splitRDD_no_stop = splitRDD.filter(lambda x: x.lower() not in stop_words)

# Create a tuple of the word and 1
splitRDD_no_stop_words = splitRDD_no_stop.map(lambda w: (w, 1))

# Count of the number of occurrences of each word
resultRDD = splitRDD_no_stop_words.reduceByKey(lambda x, y: x + y)

# example 4: print word frequencies
# Display the first 10 words and their frequencies from the input RDD
for word in resultRDD.take(10):
    print(word)

# Swap the keys and values from the input RDD
resultRDD_swap = resultRDD.map(lambda x: (x[1], x[0]))

# Sort the keys in descending order
resultRDD_swap_sort = resultRDD_swap.sortByKey(ascending=False)

# Show the top 10 most frequent words and their frequencies from the sorted RDD
for word in resultRDD_swap_sort.take(10):
    print("{},{}".format(word[1], word[0]))
