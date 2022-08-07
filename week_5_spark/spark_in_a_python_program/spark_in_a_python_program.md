# Spark in a Python program
Using Spark in a Python shell is a good way to learn about Spark, as a good way to analyse data interactively. In most 
tasks, however, we cannot simply use the shell to perform data analytics. Instead, we need to write programs in a 
separate Python file and then submit it to Spark to run. These are called self-contained applications.

Let's now learn how to do this. Let's use the word frequency task as an example.

When you click the panel on the right you will get a connection to a server that has Hadoop and YARN installed and 
running. It has a Python program called "frequencies.py", and the usual text file, "text.txt". 

You first need to create your default directory in Hadoop, and copy text.txt to it:

`hdfs dfs -mkdir -p /user/user`

`hdfs dfs -put text.txt`

Now inspect the Python program.

When using Spark in a Python shell, the SparkContext object sc is automatically created for us to use. In a 
self-contained application we need to do this ourselves. That's the first few lines of the code. The rest of the code 
counts the word frequencies and store the result to disk.

To run this program we use the spark-submit command, as follows:

`spark-submit frequencies.py`

You should see Spark begin to execute and produce the output.

After Spark completes running the job, you can see the results by listing the contents of the "results" folder:

`hdfs dfs -ls results`

You should see two files: "_SUCCESS" and "part-00000". The first file shows the status of the job, the second file 
contains the result. You can see the results by showing the contents of the second file, using the following command:

`hdfs dfs -cat results/part-00000`

You might find it convenient to move this file to your home directory on the server's local file system. You might 
like to rename it in the process - let's call it "result". Here's the command:

`hdfs dfs -get results/part-00000 result`

Now you can view the contents of the file using the much simpler command:

`cat result`
