start-dfs.sh

jps

hdfs dfs -ls

hdfs dfs -mkdir /user

hdfs dfs -mkdir /user/user

hdfs dfs -mkdir -p /user/user

hdfs dfs -ls

ls

hdfs dfs -put text.txt

hdfs dfs -ls

hdfs dfs -mkdir files

hdfs dfs -ls

hdfs dfs -mv text.txt files

hdfs dfs -ls

hdfs dfs -ls files

hdfs dfs -cp files/text.txt files/text2.txt

hdfs dfs -ls files

hdfs dfs -mv files/text2.txt files/moretext.txt

hdfs dfs -ls files

hdfs dfs -rm files/moretext.txt

hdfs dfs -ls files

hdfs dfs -cat files/text.txt

hdfs dfs -get files/text.txt text2.txt

ls
