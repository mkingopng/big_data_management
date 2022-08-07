Try it: Find top-k users (CSV data)

In your home directory on this server is a CSV file called "Comments.csv". This dataset is also 
from an anonymized dump of all user-contributed content on the Stack Exchange network. You can 
open the file to inspect its contents. The fields in the file are as follows:

```
- Id
- PostId
- Score
- Text, e.g.: "@Stu Thompson: Seems possible to me"
- CreationDate, e.g.:"2008-09-06T08:07:10.730"
- UserId
```

Your task is to find the top-3 users who have posted the most comments. The output should contain 
the top-3 users with the most comments (represented by UserId) and the number of each user’s 
comments. Please sort the result by the number of comments, and separate the UserId and the number 
of comments by "\t". Your result should be like this format:

```
7 5
5 4
6 3
```

The code template has been given in the file "top3user.py". Think about what is the most efficient 
way of solving this problem.

`cd home`

`spark-submit top3user.py "file:///home/Department.csv"`