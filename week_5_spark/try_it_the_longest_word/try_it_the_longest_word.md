# Try it: the longest word
Now try it yourself - try writing a Python program using Spark to find the length of the longest 
word in a text file.

When you click the panel on the right you will get a connection to a server that has Hadoop and 
YARN installed and running. Our text.txt file is in your home directory, and a Python program 
has been created for you, called "longest.py". You just need to fill in the details of the program.

Rather than getting your program to save the result to a text file, you might find it more 
convenient to get it to print the result instead. To do this, don't use the "saveAsTextFile()" 
command - just use an ordinary Python "print()" command instead. Note that the result will be 
printed among the many lines of program output, and it might be hard to find!

Remember that you will need to create your default directory in Hadoop, and copy text.txt to it:

`hdfs dfs -mkdir -p /user/user`

`hdfs dfs -put text.txt`

To run your program you can use the following command:

`spark-submit longest.py`

