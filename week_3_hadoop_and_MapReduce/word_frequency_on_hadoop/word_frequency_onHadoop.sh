hdfs dfs -mkdir -p /user/user
hdfs dfs -mkdir /user/user/input
hdfs dfs -put text.txt /user/user/input
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -file ~/mapper.py -mapper ~/mapper.py -file ~/reducer.py -reducer ~/reducer.py -input input -output output
hdfs dfs -cat output/part-00000
# move the results folder to your local home directory & view them there
hdfs dfs -get output output
cat output/part-00000