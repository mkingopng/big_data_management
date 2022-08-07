"""
pyspark

textfile = sc.textFile("file:///home/KVP.txt")

pair = textfile.map(lambda s: (s.split()[0],  s.split()[1]))

rdd1 = pair.mapValues(lambda x: (int(x),1))

rdd2 = rdd1.reduceByKey(lambda a,b : (a[0]+b[0],a[1]+b[1]))

res = rdd2.mapValues(lambda x: x[0]/x[1])

res.collect()
"""