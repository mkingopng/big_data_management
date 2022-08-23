# Try it: salary holders

Now try writing your own Python script using DataFrames and SQL.

When you click the panel on the right you'll get a connection to a server 
with Hadoop and YARN installed and running. In your home directory on the 
server there is the same CSV file called "employees.csv".  A Python script 
called "script.py" has been created for you.

Try writing using DataFrames and SQL to produce a list of salaries, and 
for each salary the last names of the people with that salary. You can 
use COLLECT_LIST.

https://spark.apache.org/docs/latest/api/sql/index.html#collect_list

Remember that you will need to copy employees.csv into HDFS:

> $ hdfs dfs -mkdir -p /user/user

> $ hdfs dfs -put employees.csv

You can run your Python script using the following command:

> $ spark-submit script.py
