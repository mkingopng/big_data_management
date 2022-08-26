"""

"""
from pyspark import SparkContext

sc = SparkContext

# example 1: understanding SparkContext
# Print the version of SparkContext
print("The version of Spark Context in the PySpark shell is", sc.version)

# Print the Python version of SparkContext
print("The Python version of Spark Context in the PySpark shell is", sc.pythonVer)

# Print the master of SparkContext
print("The master of Spark Context in the PySpark shell is", sc.master)

# example 1: interactive use of PySpark
# Create a Python list of numbers from 1 to 100
numb = range(1, 100)

# Load the list into PySpark
spark_data = sc.parallelize(numb)
