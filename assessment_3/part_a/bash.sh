
# part A1
python regular.py < text.txt

# part A2
# test your mapper and reducer by running the following command (it tells Python to execute mapper.py, using text.txt as
# input, and then pipe the result as input to reducer.py)
python mapper.py < text.txt | python reducer.py

# First, create your default working directory in HDFS:
hdfs dfs -mkdir -p /user/user

# Next, let's create example_file_statistics directory in which to keep the input files of our MapReduce job. Call it "input":
hdfs dfs -mkdir /user/user/input

#  third, upload the file "text.txt" into HDFS /user/user/input:
hdfs dfs -put text.txt /user/user/input

# Run the MapReduce job with the following command:
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -file ~/mapper.py -mapper ~/mapper.py -file ~/reducer.py -reducer ~/reducer.py -input input -output output

# You can view the results:
hdfs dfs -cat output/part-*

# To delete the output folder:
hdfs dfs -rm -r output