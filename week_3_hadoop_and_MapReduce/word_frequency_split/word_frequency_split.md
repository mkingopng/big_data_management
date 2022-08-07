# Word frequency, split
Now let's turn this program into one that can run on a file stored in Hadoop. We need to break it into a mapper program 
and a reducer program.

When you click the panel on the right you'll get a terminal connection to a server. On the server (in the local file 
system), are two Python programs, called "mapper.py" and "reducer.py". You can open and view them.

mapper.py takes a file from standard input and prints each word with frequency 1 to standard output. Why frequency 1? 
We'll see why shortly.

reducer.py takes a file of word-frequency pairs from standard input and prints the total frequency of each word to 
standard output.

We can simulate how Hadoop will handle this. The file "text.txt" from the previous slide has been split into two halves, 
and saved as the files "textA.txt" and "textB.txt". This is to simulate the distribution of the file across a Hadoop 
cluster. (You can open and view them.)

First, we apply mapper.py to textA.txt, and send the results to a file called results.txt (this file will be 
automatically created for you, by the local file system):

```$ python mapper.py < textA.txt > results.txt```

This command tells Python to run the program mapper.py, using the file textA.txt as the input, and then send the results 
to the file results.txt (that's what > is doing).  

Next, we do the same for textB.txt, except we append the results, by using >> instead of > (we want to keep the results 
that are already there):

```$ python mapper.py < textB.txt >> results.txt```

The file results.txt now contains the output of the mapper applied to textA.txt, and the output of the mapper applied to 
textB.txt. Finally, we apply reducer.py to results.txt to get the total frequency of each word across the two files:

```$ python reducer.py < results.txt```

This command tells Python to run the program reducer.py using the file results.txt as input.

You should see the same results as we got in the previous slide, when we applied a single Python program to the single 
text file.

What we've done here is simulated, on the local file system on the server, what MapReduce does when working with a 
distributed file in HDFS. In the next slide we'll use MapReduce. 