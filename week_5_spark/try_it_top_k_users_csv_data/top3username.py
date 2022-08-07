from pyspark import SparkContext

sc = SparkContext('local', 'top3')

# you can also receive the path of the input file from arguments
# comments_path = "file:///home/Comments.csv"
comments_path = "file://../week_5_spark/try_it_top_k_users_csv_data/comments.csv"

comments_File = sc.textFile(comments_path).map(lambda line: line.strip().split(','))
user_id = 5

# Process Comments.csv
comments_pairs = comments_File.map(lambda x: (x[user_id], 1))

id_user_pairs = comments_pairs.reduceByKey(lambda x, y: x + y)

# Return the top 3 active users
# res = sc.parallelize(id_user_pairs.sortBy(lambda x:x[1],ascending=False).take(3))

# or

res = sc.parallelize(id_user_pairs.takeOrdered(3, key=lambda x: -x[1]))
# which way is more efficient?

res.map(lambda x: f"{x[0]}\t{x[1]}").saveAsTextFile("file:///home/output")
sc.stop()
