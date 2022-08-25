# Working with local text
Let's now use Hive to work with a text file.

When you click the panel on the right you'll get a terminal connection to a 
server that has Hadoop, YARN, and Hive installed, and has the file "text.txt" 
in your home directory.

Use the following command to start a Hive shell:

> $ hive

## Create a table

Let's create a table in which to put the text file. We need to tell Hive what 
columns to have in the table, and what type of data is stored in each column 
(string, integer, date, etc.). We also need to tell it how to interpret an 
input file as having this structure. Let's think of each line in the text file 
as being a row in our table, and put the whole line into a single column called 
"line". So let's create a table using the following command:

> CREATE TABLE ourText (line STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\n' STORED AS textfile;

You can check that the table has been created by running the following command:

> SHOW TABLES;

You can check the structure of the table by running the following command:
> DESCRIBE ourText;

## Load data

Now let's load text.txt into the table:

> LOAD DATA LOCAL INPATH 'text.txt' OVERWRITE INTO TABLE ourText;

By adding the keyword "LOCAL" we are telling Hive that the file is in the 
local file system on the server (rather than in HDFS). By adding the keyword 
"OVERWRITE" we are telling Hive to replace any data that was already in the 
table (since we've just created it there shouldn't be any).

You can check that the data has been loaded by running the following command:
> SELECT * FROM ourText;

## Run queries
Now let's run some HQL queries to answer questions about the text file: 

### How many lines are in the file?

> SELECT COUNT(*) FROM ourText;

### What is the length of each line, from shortest to longest?

> SELECT LENGTH(line) FROM ourText ORDER BY LENGTH(line);

### What is the average length of the lines (in characters)?

> SELECT AVG(LENGTH(line)) FROM ourText;

### How many words are in each line of the file?

We first need to break the line into words - we can do that using Hive's 
split() function, splitting the line at its spaces. Note that we need to 
remove the empty lines by checking their length via a where clause. Then 
we can use Hive's size() function to get the number of resulting words:

> SELECT SIZE(SPLIT(line, ' ')) FROM ourText WHERE LENGTH(line)>0;

### How many words are in the file?

We can get this by summing the number of words in each line:

> SELECT SUM(SIZE(SPLIT(line, ' '))) FROM ourText WHERE LENGTH(line)>0;

### What is the average word length?
To answer this we need the total length of the words, and the number of words, 
and then divide the former by the latter. We can get the number of words 
using the previous query. What about the total length of words? We can get 
the total length of words in a line by removing its spaces (replace them 
with nothing) and then counting the number of characters that remain, then 
we can sum these to get the total length of words. So we can use the 
following query:

> SELECT SUM(LENGTH(REPLACE(line, ' ', '')))/SUM(SIZE(SPLIT(line, ' '))) FROM ourText;

# Explode
Hive has a function EXPLODE() which turns an array of values into rows. 
Try the following query:

> SELECT EXPLODE(SPLIT(line, ' ')) AS word FROM ourText;

In effect, this query generates a table of words that we can query to get 
answers about words. This involves using the above query as a subquery in 
other queries. For example:

### How many words are there?
> SELECT COUNT(*) FROM (SELECT EXPLODE(SPLIT(line, ' ')) AS word FROM ourText) AS words;

### What is the average word length?

>SELECT AVG(LENGTH(word)) FROM (SELECT EXPLODE(SPLIT(line, ' ')) AS word FROM ourText) AS words;

### What is the frequency of each word?
> SELECT word, COUNT(*) FROM (SELECT EXPLODE(SPLIT(line, ' ')) AS word FROM ourText) AS words GROUP BY word;

# Lateral View
Hive has a way of doing this more efficiently, using LATERAL VIEW. This gives 
a way of merging the results of EXPLODE back together with the original table.

>SELECT word FROM ourText LATERAL VIEW EXPLODE(SPLIT(line, ' ')) words as word;

### What are the unique words?

> SELECT DISTINCT word FROM ourText LATERAL VIEW EXPLODE(SPLIT(line, ' ')) words as word;

### What is the average word length?

> SELECT AVG(LENGTH(word)) FROM ourText LATERAL VIEW EXPLODE(SPLIT(line, ' ')) words as word;

### What is the frequency of each word?

> SELECT word, COUNT(*) FROM ourText LATERAL VIEW EXPLODE(SPLIT(line, ' ')) words as word GROUP BY word;
