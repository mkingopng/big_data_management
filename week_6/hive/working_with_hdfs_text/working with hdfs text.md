# Working with HDFS text

In the previous slide we used Hive to work with a text file in the server's local file system. Now let's now use it to 
work with a text file in HDFS.

When you click the panel on the right you'll get a terminal connection to a server that has Hadoop, YARN, and Hive 
installed and running, and has the file "text.txt" in your home directory.

## Copy to HDFS

Let's start by copying text.txt to your default directory in HDFS:

> $ hdfs dfs -mkdir -p /user/user

> $ hdfs dfs -put text.txt

## Start hive

Use the following command to start a Hive shell:

> $ hive

# Create the table
Create the table as before:
> CREATE TABLE ourText (line STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\n' STORED AS textfile;

## Load data
Now let's load text.txt into the table, this time loading it from HDFS:

> LOAD DATA INPATH 'text.txt' OVERWRITE INTO TABLE ourText;

Since we have not added the "LOCAL" keyword Hive will look for the file text.txt in your default HDFS directory.

You can check that the data has been loaded by running the following command:

> SELECT * FROM ourText;

## Run queries
Now we can run queries as before. Let's get **the frequency of words in the file**. Last time we did this in two ways. 
Try each one:

> SELECT word, COUNT(*)
FROM (SELECT EXPLODE(SPLIT(line, ' ')) AS word FROM ourText) AS words
GROUP BY word;
 
> SELECT word, COUNT(*)
FROM ourText LATERAL VIEW EXPLODE(SPLIT(line, ' ')) words as word
GROUP BY word;
