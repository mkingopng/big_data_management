# Try it: unique lines

The previous example showed how to write a MRJob program that produces a list of unique words in a file. Try modifying 
that job into one that produces a list of unique lines instead. For example, if an input file is this:

```
2013-11-01 aa
2013-11-02 bb
2013-11-03 cc
2013-11-01 aa
2013-11-03 dd
2013-11-02 bb
```

Your job will output these contents (the duplicate rows have been removed, ignored the order and quotation marks):
```
2013-11-01 aa
2013-11-02 bb
2013-11-03 cc
2013-11-03 dd
```

You can run your job using the following command:

`python job.py text.txt`
