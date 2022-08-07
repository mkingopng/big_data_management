# Try it: word average length

Given a text file, compute the average length of words starting with each alphabetical letter "a" to "z". This means 
that for every letter, you need to compute: the total length of all words that start with the letter divided by the 
total number of words that start with the letter.
- Ignore the letter case, i.e., first convert all words to lower case (using the `lower()` function).
- Ignore terms starting with non-alphabetical characters, i.e., only consider words starting with “a” to “z”.
- You can use the space character to split the documents into words (like `line.split(" ")`).
- Sort the final result based on the alphabetical order (use the `sortBy()` operation or the `sortByKey()` operation).

For example, given "This is a test", we have one word starting with "a", one word starting with "i", and two words 
starting with "t". Thus, the result is like (a, 1), (i, 2), and (t, 4).

Your program could take two arguments receiving from the command line, the first one is the input text file and 
the second one is the output folder. For example,  to run your program you can use the following command:

`hdfs dfs -mkdir -p /user/user`

`hdfs dfs -put text.txt`

`spark-submit word_average.py "file:///home/text.txt" "file:///home/output"`

Next, you can enter the output directory in your home folder to check the results using the "cat" command.

The code template and the text file are provided to you. The final result should be like below (the saveAsTextFile() 
operation by default includes a pair of parentheses in each line, and thus you need to use Python to change the output 
format):

```
a, 3.0
b, 4.8
c, 6.285714285714286
d, 7.133333333333334
e, 6.5
f, 4.7368421052631575
g, 5.5
h, 4.9375
i, 2.6153846153846154
l, 5.5
m, 4.4
n, 4.411764705882353
o, 2.1818181818181817
p, 6.5
r, 7.333333333333333
s, 4.583333333333333
t, 3.558139534883721
u, 5.2
v, 9.0
w, 3.380952380952381
y, 5.0
```
