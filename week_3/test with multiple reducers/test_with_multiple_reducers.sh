# preparation
hdfs dfs -mkdir -p /user/user
hdfs dfs -mkdir /user/user/input
hdfs dfs -put employees.csv /user/user/input

# running the job with example_file_statistics single reducer
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -file ~/mapper.py -mapper ~/mapper.py -file ~/reducer.py -reducer ~/reducer.py -input input -output output
hdfs dfs -ls output
hdfs dfs -cat output/part-00000

# running the job with 3 reducers
hdfs dfs -rm -r output
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -file ~/mapper.py -mapper ~/mapper.py -file ~/reducer.py -reducer ~/reducer.py -numReduceTasks 3 -input input -output output
hdfs dfs -ls output
hdfs dfs -cat output/part-*