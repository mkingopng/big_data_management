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

csv_path = r'assessment_5_and_6/orders.csv'

raw_df = spark.read.option('header', True).csv(csv_path)
raw_df = raw_df.withColumn('Quantity', raw_df['Quantity'].cast(IntegerType()))

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



