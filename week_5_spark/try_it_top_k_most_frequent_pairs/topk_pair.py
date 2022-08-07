import sys

from pyspark import SparkContext, SparkConf


def pairGen(line):
    pairList = []
    words = line.strip().lower().split(" ")
    for i in range(len(words)):
        ti = words[i]
        for j in range(i + 1, len(words)):
            tj = words[j]
            if ti <= tj:
                pairList.append(ti + "," + tj)
            else:
                pairList.append(tj + "," + ti)
    return pairList


if __name__ == "__main__":
    k = int(sys.argv[1])
    sc = SparkContext("local", "topk pair")
    textfile = sc.textFile("file:///home/text.txt")
    pairs = textfile.flatMap(pairGen).map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)
    # res = pairs.sortBy(lambda x:x[0]).sortBy(lambda x: x[1], False).take(k)
    # res = pairs.sortBy(lambda x:(-x[1], x[0])).take(k)
    res = pairs.takeOrdered(k, key=lambda x: (-x[1], x[0]))
    topk = sc.parallelize(res)
    topk.saveAsTextFile("file:///home/output")
    sc.stop()