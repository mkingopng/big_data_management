# map() vs flatmap()
Assume we have a file containing two lines:

```
This is the first sentence.
This is the second sentence.
```

First, enter the pyspark shell using the command `pyspark`. Next, we load the file into an RDD. This time we load the 
file directly from your local file system, rather than HDFS

`file = sc.textFile("file:///home/text.txt")`

`file.collect()`

Next, we use map and flatmap to operate the file. 

`file.map(lambda x: x.split(" ")).collect()`

You can see the result as:

```[['This', 'is', 'the', 'first', 'sentence.'], ['This', 'is', 'the', 'second', 'sentence.']].```

`file.flatMap(lambda x: x.split(" ")).collect()`

You can see the result as:

```['This', 'is', 'the', 'first', 'sentence.', 'This', 'is', 'the', 'second', 'sentence.'].```

From this example, you could understand why we use flatMap rather than map in the word count problem.