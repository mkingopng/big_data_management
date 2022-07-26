# Word frequency (Hadoop)
When you click the panel on the right you will get a terminal connection to a server which has Hadoop and YARN 
installed and running. It also has the text.txt file and the job.py MRJob program from the previous slide.

You can choose whether to run job.py locally on the server or instead of the server's Hadoop cluster.

## Run locally
You've already seen how to run it locally:

```$ python job.py < text.txt```

## Run on Hadoop
To run it on the Hadoop cluster use the following command instead:

```$ python job.py -r hadoop < text.txt```

Here you are adding the -r option to your command ("r" is for "runner"). You can use -r inline (the default), 
-r local (which simulates some features of Hadoop), or -r hadoop (which runs your job on Hadoop).

Note that you can observe that the results are different when running on Hadoop. The reason is that, Hadoop will 
perform shuffling and sorting for the mapper output. The mapper output is received by the reducers with orders, and 
thus the final results are sorted by keys. However, if you run MRJob codes locally, Hadoop is not involved in this 
procedure, and the mapper output is thus not sorted. Therefore, if your reducer procedure depends on the order of the 
received mapper output, you must run and test your codes on Hadoop to check the correctness.

Note that it is much slower on Hadoop. In the rest of these slides we'll just run jobs locally, which is good for 
learning and testing, since these jobs do not rely on the mapper output's order.

## Run on Hadoop with HDFS file
In the last example we ran job.py on the Hadoop cluster but we passed it a local file (that is, a file stored on 
the server's local file directory). You call also pass it a file stored in HDFS. Let's see how to do that.

First, create your default directory in HDFS and copy the file to it:

```$ hdfs dfs -mkdir -p /user/user```

```$ hdfs dfs -put text.txt```

Now pass this file to job.py by using the following command:

```$ python job.py -r hadoop hdfs:///user/user/text.txt```

You can also store the output in HDFS by using the "-o" option in your command:

```$ python job.py -r hadoop hdfs:///user/user/text.txt -o hdfs:///user/user/output```

After your job completes, you can check the results in HDFS by:

```$ hdfs dfs -cat output/p*```

Run locally with HDFS file?

You can't do that. Try it:

```$ python job.py hdfs:///user/user/text.txt```
