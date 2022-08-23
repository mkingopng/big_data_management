
# create directory
# hdfs dfs -mkdir -p /user/user

# move the data file into the directory
# hdfs dfs -put employees.csv

# submit the Python program to Spark
# spark-submit program.py

# get Spark to save the results to a file by replacing results.show() with the following line
# results.write.format("csv").save('output')

# hdfs dfs -ls output

# see the results by listing the contents of the "output" folder
# hdfs dfs -cat output/part-*

# see the results by showing the contents of the second file, using the following command
# hdfs dfs -get output/part-* result.csv

# view the contents of the file using the much simpler command
# cat result.csv
