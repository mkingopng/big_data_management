# DataFrames in a Python program

Now let's see how to use DataFrames in a Python program.

If you click on the panel on the right you will get a terminal connection to a server 
with Hadoop and YARN installed and running. In your home directory on the server 
there is the same CSV file called "employees.csv".  And there is also a Python program 
called "program.py".

To work with this file using Spark we need to put it into HDFS:
> $ hdfs dfs -mkdir -p /user/user
 
> $ hdfs dfs -put employees.csv

Now we can submit the Python program to Spark:

> $ spark-submit program.py

You should see Spark begin to execute and produce the output.

# Saving output to a file

At the moment the Python program asks Spark to show the results in the terminal 
window. You can also get Spark to save the results to a file. You can do that by 
replacing results.show() with the following line:
> results.write.format("csv").save('output')

This tells Spark to save the results in CSV format, in a folder called "output" 
in your default directory in HDFS (it will create this for you).

Now run the program again, as per above. This time the results will be saved to HDFS.

After Spark completes running the program, you can see the results by listing the 
contents of the "output" folder:

> $ hdfs dfs -ls output

You should see two files: "_SUCCESS" and one that starts with "part-". The first 
file shows the status of the program, the second file contains the result. You can 
see the results by showing the contents of the second file, using the following 
command:

> $ hdfs dfs -cat output/part-*

You might find it convenient to move this file to your home directory on the 
server's local file system. You might like to rename it in the process - let's 
call it "result". Here's the command:

> $ hdfs dfs -get output/part-* result.csv

Now you can view the contents of the file using the much simpler command:

> $ cat result.csv
 