# Hive

You've now had some experience writing mapper and reducer programs and getting 
them to run as a MapReduce job on Hadoop. 

You've also had some experience using Python's MRJob class, which simplifies 
the process of writing and running mappers and reducers.

As you've probably noticed, figuring out how to extract the information that 
you want from the data using mappers and reducers can take quite a bit of 
ingenuity and work. Wouldn't it be nice if you could use something like SQL to 
get those answers instead? Writing SQL statements is much more intuitive and 
much simpler than writing mappers and reducers.

As it turns out, you can. 

By 2007, Facebook had a lot of programmers with experience using SQL to query 
data, but not much experience using Java or writing MapReduce jobs. So they 
developed a way to convert SQL queries into MapReduce jobs. The result was some 
software called Hive. Hive has been so popular that it is now an open source 
application within the Apache Software Foundation, and is one of their 
top-level projects. It is now used by companies such as Netflix and Amazon.

Hive doesn't quite use SQL - it uses its own version, called Hive Query 
Language (HiveQL, HQL). HQL is more limited than SQL - it has a data definition 
language and a data manipulation language, but each is more limited than those 
of SQL. 

For example, the DML does not allow row-level inserts, updates, or deletes, and 
there is limited support for sub queries.

Hive allows you to think about the data you have stored in HDFS as though it 
were in a relational database, by projecting table-like structure onto it. 
This structure is stored in a relational database known as the metastore; you 
can think of the metastore as being like the schema of your would-be relational 
database. Note, however, that your data is not in a relational database, and 
Hive is not a relational database management system - it might look that way, 
because of HQL, but behind the scenes is just Hadoop and MapReduce.

Hive has a driver that manages the lifecycle of an HQL statement as it gets 
processed by Hive:
- Query Compiler: compiles the HQL into MapReduce tasks
- Optimizer: generates the best execution plan
- Execution Engine: executes the tasks produced by the compiler in the 
appropriate order, by interacting with Hadoop

The next two slides contain a couple of video introductions to Hive. Then, in 
the slides after that, you'll get some hands-on experience using Hive.

# Hive Built-in Functions
In Hive, there are some built-in functions available. We have used some Hive 
built-in functions such as split(), size(), length(), etc. We can use these 
functions to do various tasks in our applications. 

There are several types of Hive Built-in Functions available, including:
- Mathematical Functions https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-MathematicalFunctions
- Collection Functions https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-CollectionFunctions
- Type Conversion Functions https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-TypeConversionFunctions
- Date Functions https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-DateFunctions
- Conditional Functions https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-ConditionalFunctions
- String Functions https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-StringFunctions
- Data Masking Functions https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-DataMaskingFunctions
- Misc. Functions https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-Misc.Functions

The function explode() is a type of the Built-in Table-Generating Functions (UDTF). 

https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-Built-inTable-GeneratingFunctions(UDTF)

If these functions are not sufficient to do your task, you can also define your 
own user-defined functions (UDF). For more details, please refer to this page 
at Hive's official website: LanguageManual UDF.

https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF

Below are some commonly used built-in string functions:

| Function Name                 | Return Type | Description                                                                                                                                                    |
|-------------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| reverse(string X)             | string | It will give the reversed string of X                                                                                                                          |
| rtrim(string X)               | string | It will fetch and returns the string resulting from trimming spaces from the end (right-hand side) of X For example, rtrim(‘ results ‘) results in ‘ results’  |
| space(INT n)                  | string | It will fetch and gives a string of n spaces.                                                                                                                  |
| split(STRING str, STRING pat) | array | Splits str around pat (pat is a regular expression).                                                                                                           |
|  substr(string binary A, int start, int len) | string | It will return the substring or slice of the byte array of A starting from start position with length len. For example, substr('foobar', 4, 1) results in 'b'. |


# Further resources
The official Hive website is a good source for further information about Hive:

Official Hive website: https://hive.apache.org/

You might find this Hive cheatsheet by Hortonworks a convenient reference:

Hive cheatsheet by Hortonworks: http://hortonworks.com/wp-content/uploads/2016/05/Hortonworks.CheatSheet.SQLtoHive.pdf
