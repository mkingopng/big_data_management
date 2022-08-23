# Try it: Rank the terms by their frequencies

Let's use Spark SQL to compute the frequency for each term within each year 
again. Sort the result by the year first, and then by the frequency in descending 
order. For the terms with the same frequency, rank them in alphabetical order.

- First, you can use the `spark.read.text()` function to read the file into a 
DataFrame object. 

- Next, you can use the `selectExpr()` function to separate the 
single line column into two columns in a new DataFrame object. 

- You can use DataFrame's `orderBy()` function to sort the results. Please try 
to use your SQL knowledge to solve this problem.

More DataFrame APIs can be found at this page:

https://spark.apache.org/docs/3.2.0/api/python/reference/pyspark.sql.html#dataframe-apis.

use this command to execute your program
> spark-submit script.py