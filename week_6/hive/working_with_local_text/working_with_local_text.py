from pyhive import hive

cursor = hive.connect('localhost').cursor()

# start a hive shell
# $ hive

# create a table using the following command:
cursor.execute('CREATE TABLE ourText (line STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\n' STORED AS textfile;')

# check that the table has been created by running the following command:
cursor.execute('SHOW TABLES;')

# check the structure of the table by running the following command:
cursor.execute('DESCRIBE ourText;')

# load text.txt into the table:
cursor.execute('LOAD DATA LOCAL INPATH "text.txt" OVERWRITE INTO TABLE ourText;')

# check that the data has been loaded by running the following command:
cursor.execute('SELECT * FROM ourText;')

# How many lines are in the file?
cursor.execute('SELECT COUNT(*) FROM ourText;')

# What is the length of each line, from shortest to longest?
cursor.execute('SELECT LENGTH(line) FROM ourText ORDER BY LENGTH(line);')

# What is the average length of the lines (in characters)?
cursor.execute('SELECT AVG(LENGTH(line)) FROM ourText;')

# How many words are in each line of the file?
cursor.execute('SELECT SIZE(SPLIT(line, ' ')) FROM ourText WHERE LENGTH(line)>0;')

# How many words are in the file?
cursor.execute('SELECT SUM(SIZE(SPLIT(line, ' '))) FROM ourText WHERE LENGTH(line)>0;')

# What is the average word length?
cursor.execute('SELECT SUM(LENGTH(REPLACE(line, ' ', '')))/SUM(SIZE(SPLIT(line, ' '))) FROM ourText;')

# Explode
cursor.execute('SELECT EXPLODE(SPLIT(line, ' ')) AS word FROM ourText;')'

# How many words are there?
cursor.execute('SELECT COUNT(*)FROM (SELECT EXPLODE(SPLIT(line, ' ')) AS word FROM ourText) AS words;')

# What is the average word length?
cursor.execute('SELECT AVG(LENGTH(word)) FROM (SELECT EXPLODE(SPLIT(line, ' ')) AS word FROM ourText) AS words;')

# What is the frequency of each word?
cursor.execute('SELECT word, COUNT(*) FROM (SELECT EXPLODE(SPLIT(line, ' ')) AS word FROM ourText) AS words GROUP BY word;')

# lateral view
cursor.execute('SELECT word FROM ourText LATERAL VIEW EXPLODE(SPLIT(line, ' ')) words as word;')

# What are the unique words?
cursor.execute('SELECT DISTINCT word FROM ourText LATERAL VIEW EXPLODE(SPLIT(line, ' ')) words as word;')'

# What is the average word length?
cursor.execute('SELECT AVG(LENGTH(word)) FROM ourText LATERAL VIEW EXPLODE(SPLIT(line, ' ')) words as word;')

# What is the frequency of each word?
cursor.execute('SELECT word, COUNT(*) FROM ourText LATERAL VIEW EXPLODE(SPLIT(line, ' ')) words as word GROUP BY word;')
