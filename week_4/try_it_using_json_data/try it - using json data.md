# Try it: using JSON data
Now try for yourself using MRJob to work with JSON data.

When you click the panel on the right you'll get a connection to a server that has the same JSON file as the last slide 
in your home directory, "data.json". Again, you can open the file to inspect the data.

First, try writing a MRJob program that **counts the total number of enrolments**. So the result should be this:
```Total enrolments: 18```

A file called "job1.py" has been created for you, in which to write your program. You can test it using the following 
command:

`python job1.py data.json`

Second, try writing a MRJob program that **lists the students who are in each course**. So the results should be these:
```
ZZEN9021: Jamie
ZZEN9311: Natalie, Sam, Tom
ZZEN9313: Jamie, Natalie, Sam, Tom
ZZSC5806: Natalie, Sam, Sarah, Tom
ZZSC5905: Natalie, Sam, Sarah, Tom
ZZSC9001: Sarah, Tom
```

A file called "job2.py" has been created for you, in which to write your program. You can test it using the following 
command:

`python job2.py data.json`
