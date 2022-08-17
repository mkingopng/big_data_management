import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    #
    inputfile = sys.argv[1]
    #
    output = sys.argv[2]
    #
    sc = SparkContext("local", "word average length")
    #
    textfile = sc.textFile(inputfile)
    #
    words = textfile.flatMap(lambda x: x.split(" ")).map(lambda x: x.lower())
    #
    finalwords = words.filter(lambda x: len(x) > 0 and 'a' <= x[0] <= 'z')
    #
    len_count = finalwords.map(lambda x: (x[0], (len(x), 1))).reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))
    #
    avgLen = len_count.map(lambda x: (x[0], x[1][0] / x[1][1]))
    #
    res = avgLen.sortBy(lambda x: x[0]).map(lambda x: f'{x[0]}, {x[1]}')
    #
    res.saveAsTextFile(output)
    #
    sc.stop()


# create default directory in hadoop
# hdfs dfs -mkdir -p /user/user

# copy the txt file to it
# hdfs dfs -put text.txt

# to run the file
# spark-submit word_average.py "file:///home/text.txt" "file:///home/output"

# see output directory for part-00000
