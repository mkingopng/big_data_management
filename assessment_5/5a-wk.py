"""
DESCRIPTION

Copyright (C) Weicong Kong, 26/08/2022
"""

import os
import sys

from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext

# WKNOTE: solution for pyspark Cannot run program "python3", set the following environment variables in your code
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.getOrCreate()
# sql_context = SQLContext(spark.sparkContext)

sc = spark.sparkContext

abc_news = r'assessment_5_and_6/abcnews.txt'
stop_words_path = r'assessment_5_and_6/stopwords.txt'
output = r'output'


def get_words(line):
	ts, text = line.split(',')
	words = text.split()
	return words


lines = sc.textFile(abc_news)
lines.first()


def read_stop_words():
	with open(stop_words_path, 'r') as f:
		t = f.read()
	stop_words = t.split()
	return stop_words


words_rdd = lines.flatMap(get_words)

# Top 10 most frequent words:
print(words_rdd.map(lambda x: (x, 1)).groupByKey().mapValues(sum).map(lambda x: (x[1], x[0])).sortByKey(False).take(10))



lines = sc.textFile(abc_news)


def deal_with_line(line):
	ts, text = line.split(',')
	year = ts[:4]
	words = text.split()
	res = []
	for w in words:
		res.append((year, w, 1))
	return res


year_word_pair = lines.flatMap(deal_with_line)
print(year_word_pair.count())

STOP_WORDS = read_stop_words()
no_stop_words = year_word_pair.filter(lambda x: x[1].lower() not in STOP_WORDS)
print(no_stop_words.count())
print(no_stop_words.take(5))


groups = no_stop_words.groupBy(lambda x: (x[0], x[1]))
print([(k, list(v)) for k, v in groups.take(5)])


def sum_counts(tups):
	res = 0
	for t in tups:
		res += t[-1]
	return res


counts = groups.mapValues(sum_counts)


remapped = counts.map(lambda x: (x[0][0], (x[0][1], x[1])))
print(remapped.take(5))


def take_top_n_words(tuples, n):
	sorted_tuples = sorted(tuples, key=lambda x: (-int(x[1]), x[0]))
	if n <= len(sorted_tuples):
		return sorted_tuples[:n]
	else:
		return sorted_tuples


final_with_count = remapped.groupByKey().mapValues(lambda x: take_top_n_words(x, 3))

final = final_with_count.mapValues(lambda x: ' '.join(map(lambda y: y[0], x))).collect()

for k, v in final:
	print(k, '\t', v)

