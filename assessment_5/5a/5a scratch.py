"""
I am now getting an output, so something is heading in the right direction
There are several problems:
    - i get 2 return files not 1
    - I'm only getting letters, not full words
    - i haven't included the years as the key yet
    - i haven't got the top-k functionality yet
"""

# from pyspark import SparkContext
#
# # abc_news = 'file:///home/abcnews.txt'
# # stop_words = 'file:///home/stopwords.txt'
# # output = 'file:///home/output'
#
#
# stop_words = 'stopwords.txt'
# output = 'scratch_output'
#
# sc = SparkContext()
#
# baseRDD = sc.textFile(abc_news)

# this works in base python
abc_news = 'assessment_5/5a/abcnews.txt'
with open(abc_news) as file:
    while line := file.readline().rstrip():
        ts, text = line.split(',')
        year = ts[:4]
        words = text.split()
        for word in words:
            print(word, (year, 1))



# date_list = []

# # the dates are left of the comma
# for line in lines:
#     dates = line.map(lambda lines: lines.split(',')[0])
# dates.append(date_list)
#
# # the text is right of the comma
# text = baseRDD.map(lambda line: line.split(',')[1])
#
# split the text on spaces
# wordsRDD = text.map(lambda text: text.split(' '))

# Convert the words in lower case & remove stop words from the stop_words list
# splitRDD_no_stop = wordsRDD.filter(lambda x: x.lower() not in stop_words)

# # Create a tuple of the word and 1
# splitRDD_no_stop_words = splitRDD_no_stop.map(lambda w: (w, 1))
#
# # Count of the number of occurrences of each word
# resultRDD = splitRDD_no_stop_words.reduceByKey(lambda x, y: x + y)
#
# # save the output
# resultRDD.saveAsTextFile(output)

# sc.stop()

# ----------
#
# $ hdfs dfs -mkdir -p /user/user

#
# $ hdfs dfs -put abcnews.txt

# $ hdfs dfs -put stopwords.txt

#
# spark-submit rdd.py

# ------------------------

#
# $ hdfs dfs -put Comments.csv

#
# spark-submit top3user.py

# --------