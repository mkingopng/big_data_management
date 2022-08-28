"""
DESCRIPTION

Copyright (C) Weicong Kong, 27/08/2022
"""


import os
import sys

from operator import add

from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext

# WKNOTE: solution for pyspark Cannot run program "python3", set the following environment variables in your code
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.getOrCreate()
# sql_context = SQLContext(spark.sparkContext)

sc = spark.sparkContext

csv_path = r'assessment_5_and_6/orders.csv'


csv_rdd = sc.textFile(csv_path)

no_header_rdd = csv_rdd.filter(lambda x: x.split(',')[0] != 'OrderDate')


def read_csv(line):

	data = tuple(line.split(','))

	return data


data_rdd = no_header_rdd.map(read_csv)

date_and_count = data_rdd.map(lambda x: (x[0], int(x[5])))

daily_sum = date_and_count.reduceByKey(add)

final_rdd = daily_sum.sortBy(lambda x: (-int(x[1]), x[0]))

print('\n')
for d, q in final_rdd.collect():
	print(f'{d},{q}')


# using pandas
import pandas as pd

df = pd.read_csv(csv_path)
result = df.pivot_table(index='OrderDate', values='Quantity', aggfunc=sum).reset_index().sort_values(
	by=['Quantity', 'OrderDate'], ascending=[False, True])
print(result)
