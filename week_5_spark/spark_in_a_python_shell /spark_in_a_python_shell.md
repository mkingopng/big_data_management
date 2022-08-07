# Spark in a Python shell
Let's see how to use Spark in a Python shell. We'll use it to explore a text file, including our usual example - the 
frequency of words in the file.

When you click the panel on the right you'll get a connection to a server with Hadoop and YARN installed and running.

## Upload a file to HDFS
In your home directory on the server there is the file "text.txt". To work with this file using Spark we need to put 
it into HDFS. Use the following commands, with which you should be familiar by now:

`hdfs dfs -mkdir -p /user/user`

`hdfs dfs -put text.txt`

## Start a Python shell
You can get a Python shell, with Spark loaded for you, using the following command:

`pyspark`

## Exploring the file
Python is now running with a SparkContext object sc created for you. You can run Spark commands directly using at the command line.

First, create an RDD:

`text = sc.textFile("text.txt")`

You now have an RDD called "text" which contains the contents of the file "text.txt". To see the number of items in the RDD you can use the count() action: 

`text.count()`

To see the first item of the RDD you can use the first() action:

`text.first()`
