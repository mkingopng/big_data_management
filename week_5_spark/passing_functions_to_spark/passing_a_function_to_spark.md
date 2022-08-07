# Passing functions to Spark
As shown in the previous examples, you can see that Spark’s API relies heavily on passing functions in the 
driver program to run on the cluster. There are three recommended ways to do this:

- Lambda expressions, for simple functions that can be written as an expression. (Lambdas do not support 
multi-statement functions or statements that do not return a value.) For example, `reduceByKey(lambda a, b: a+b)`

- Local defs inside the function calling into Spark, for longer code. For example, in pyspark:

```
>>>def containsError(s): 

...     return "HDFS" in s 

...

>>> msg = errors.filter(containsError)
```

- Top-level functions in a module. For example, as you can see in the file "passfunc.py", we define a function 
myFunc(s) which takes a string as input, and it splits the string using the space character, and returns the 
number of words obtained from this string. This function can be passed to the `map()` operation. Run the code by 
running `spark-submit passfunc.py`. Then, check the results by `cat output/part-00000`

# steps:

`spark-submit passfunc.py`

`cat output/part-00000`
