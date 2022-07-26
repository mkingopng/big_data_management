# Word frequency, on Hadoop

Now let's get this to run as a MapReduce job on Hadoop.

When you click the panel on the right you will get a terminal connection to a server that has Hadoop installed and 
running, and also YARN (which is a part of Hadoop that is needed to run MapReduce jobs).

## Preparation
We need to copy the file text.txt into HDFS.

First, create your default working directory in HDFS:

```$ hdfs dfs -mkdir -p /user/user```

Next, let's create a directory in which to keep the input files of our MapReduce job. Call it "input":

```$ hdfs dfs -mkdir /user/user/input```

Upload the file "text.txt" into HDFS /user/user/input:

```$ hdfs dfs -put text.txt /user/user/input```

## Running the job
Now let's run the MapReduce job.

```$ hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -file ~/mapper.py -mapper ~/mapper.py -file ~/reducer.py -reducer ~/reducer.py -input input -output output```

The Hadoop streaming utility will create a MapReduce job, submit the job to an appropriate cluster and monitor the 
progress of the job until it completes.

The results of the job will be put in the HDFS folder /output. You can view the results there. You will see a file with 
the name "part-00000", which contains the result.

```$ hdfs dfs -cat output/part-00000```

Alternatively, you could move the results folder to your local home directory and view them from there:

```$ hdfs dfs -get output output```

```$ cat output/part-00000```

## Explaining the mapper code

1. The first line cannot be deleted in the mapper/reduce script!

```#!/usr/bin/python```

Only Java is the native programming language for MapReduce. If we want to use the other languages to program with 
MapReduce, we always need to do it via Hadoop streaming. This line tells the operating system to use "python" when 
running the mapper script to get the input from stdin and to generate the mapper output to stdout, which will be 
received by the reducer later. In fact, you can use a Python script as the mapper, and use another programming language 
to write the reducer script.

2. The "sys" module in Python provides various functions and variables that are used to manipulate different parts of 
the Python runtime environment. It allows operating on the interpreter as it provides access to the variables and 
functions that interact strongly with the interpreter. You can read more details at 
https://docs.python.org/3/library/sys.html and https://www.geeksforgeeks.org/python-sys-module/. 

Hadoop streaming reads the data from HDFS and then feeds the data as a stream to stdin. We need to use the "sys" module 
because we need to get data from sys.stdin in the mapper script.

3. The for loop is used to get the texts from stdin in an iterative manner. In each iteration of the for loop, we can 
get one line from stdin, and you decide how to deal with this line in the mapper code.

4. In line 4, we process each line from the file stored in HDFS, i.e., "text.txt". ```line.strip().split()``` generates an 
array of strings. The ```strip()``` method removes any leading (spaces at the beginning) and trailing (spaces at the end) 
characters. The ```split()``` method splits a string into a list. You can specify the separator, and the default 
separator is any whitespace.

5. Finally, for each word we have obtained, we create a key-value pair, in which the key is the word itself and the 
value is 1, representing 1 occurrence of the word in the file. Remember that the data structure used in MapReduce is 
always in the format of key-value pairs. Thus, in your mapper, you always need to generate the output in this format. 
Hadoop streaming divides the mapper output into keys and values by the tab character by default. Thus, with this mapper 
code, MapReduce will use the words as the keys and the 1s as the values.

You can only run the mapper script to see the mapper output in HDFS. This can help you debug the mapper code.
```$ hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -file ~/mapper.py -mapper ~/mapper.py -input input -output Mapperoutput```

## Explaining the reducer code

1. Hadoop streaming converts the key/values pairs from mapper output into lines and feeds these lines to the stdin of 
the reducer process. 

For the usage of ```split()```, you can refer to this link for more examples: https://www.tutorialgateway.org/python-split/. 
Here, ```split('\t', 1)``` is not quite necessary since we can guarantee that in the reducer, each line we received from stdin 
is in the format of ```word + "\t" + "1"```. However, in some other tasks, you may need to think about how to decompose the 
reducer input into keys and values correctly.

2. We use a dictionary object to store the counts of words. If you are not familiar with the Python dictionary, you can 
refer to this link for more example usages: https://www.w3schools.com/python/python_dictionaries.asp. 

3. ```words.sort()``` aims to make sure that the reducer output is sorted by the words. You can ignore this line if the 
order of your final results does not matter.

4. Finally, we use ```print(word, results[word])``` to print both the word and its count to stdout. By default, 
```print()``` uses the space character to separate multiple fields. If you want to use the tab character as the 
separator, you can do like ```print(word, results[word]sep='\t')```. Hadoop streaming will write the data from stdout 
to HDFS finally. 