"""
DESCRIPTION

Copyright (C) Weicong Kong, 28/08/2022
"""

import os
import sys

from operator import add

from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.types import IntegerType, DateType

# WKNOTE: solution for pyspark Cannot run program "python3", set the following environment variables in your code
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.getOrCreate()
# sql_context = SQLContext(spark.sparkContext)

sc = spark.sparkContext

csv_path = r'assessment_5_and_6/cases-locations.csv'

raw_df = spark.read.option('header', True).csv(csv_path)

print(raw_df.schema)
raw_df = raw_df.withColumn('notification_date', raw_df['notification_date'].cast(DateType()))
raw_df = raw_df.withColumn('postcode', raw_df['postcode'].cast(IntegerType()))
raw_df = raw_df.withColumn('num', raw_df['num'].cast(IntegerType()))

raw_df.createOrReplaceTempView('case_locations')

sql = """
with all_lhd_daily_increase as (
select lhd_2010_name, lhd_2010_code, notification_date, sum(num) as total_num
from case_locations
group by lhd_2010_name, lhd_2010_code, notification_date
), daily_ranking as (
select *, rank() over (partition by lhd_2010_code order by total_num desc) as ranking 
from all_lhd_daily_increase
)

select lhd_2010_name, lhd_2010_code, notification_date, total_num
from daily_ranking
where ranking = 1
order by total_num desc, notification_date, lhd_2010_name desc
"""
spark.sql(sql).show()
