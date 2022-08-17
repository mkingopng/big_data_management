import sys

from pyspark import SparkContext, SparkConf


if __name__ == "__main__":
    #
    def my_func(s):
        """

        :param s:
        :return:
        """
        words = s.split(" ")
        return len(words)

    #
    sc = SparkContext("local", "word average length")
    #
    textfile = sc.textFile("file:///home/text.txt")
    #
    res = textfile.map(my_func)
    #
    res.saveAsTextFile("file:///home/output")
    #
    sc.stop()


# create default directory in hadoop
# hdfs dfs -mkdir -p /user/user

# copy the txt file to it
# hdfs dfs -put text.txt

# to run the file
# spark-submit passfunc.py
