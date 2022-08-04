import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    def myFunc(s):
        words = s.split(" ")
        return len(words)


    sc = SparkContext("local", "word average length")
    textfile = sc.textFile("file:///home/text.txt")
    res = textfile.map(myFunc)
    res.saveAsTextFile("file:///home/output")
    sc.stop()