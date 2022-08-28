"""
DESCRIPTION

Copyright (C) Weicong Kong, 28/08/2022
"""

import os
import sys

from operator import add

from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.types import IntegerType

# WKNOTE: solution for pyspark Cannot run program "python3", set the following environment variables in your code
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.getOrCreate()
# sql_context = SQLContext(spark.sparkContext)

sc = spark.sparkContext

csv_path = r'assessment_6/6b -spark SQL with CSV/orders.csv'

# WKNOTE: better way of adding the headers, and infer the data type
raw_df = spark.read.csv(csv_path, header=True, inferSchema=True)
raw_df.printSchema()

# use spark dataframe
df = raw_df.groupBy('OrderDate').sum('Quantity')
result = df.sort(['sum(Quantity)', 'OrderDate'], ascending=[False, True])
print(result.show())

# use spark SQL
raw_df.createOrReplaceTempView('order')
sql = """
select OrderDate, sum(Quantity) as Quantity
from order
group by OrderDate
order by Quantity desc, OrderDate
"""
spark.sql(sql).show()



