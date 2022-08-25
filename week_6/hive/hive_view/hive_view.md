# Hive View

In SQL, a view is a virtual table based on the result-set of an SQL statement. 
A view contains rows and columns, just like a real table. The fields in a view 
are fields from one or more real tables in the database. You can add SQL 
statements and functions to a view and present the data as if the data were 
coming from one single table.

In Hive, you can also create a view to facilitate your task. We can query a 
view just like querying a table. First, let's create a table and load the data:

> CREATE TABLE doc(line STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\n' STORED AS textfile; 
> LOAD DATA LOCAL INPATH 'text.txt' OVERWRITE INTO TABLE doc;

Given the task of finding the maximum length of words in the given file, we can 
first create a view to store the words in a virtual table:

> CREATE VIEW words AS SELECT EXPLODE(SPLIT(line, ' ')) AS word FROM doc;

Now, you can just treat words as a table and do the task:

> SELECT MAX(LENGTH(word)) FROM words;

To drop an existing view, you can do like this:

> DROP VIEW words;
