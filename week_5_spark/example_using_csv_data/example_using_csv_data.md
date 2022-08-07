# Example: using CSV data

Now let's try working with a CSV file. In your home directory on this server is a CSV file 
called "Votes.csv". This dataset is from an anonymized dump of all user-contributed content 
on the Stack Exchange network.

You can open the file to inspect its contents. The fields in the file are as follows:
* Id
* PostId
* VoteTypeId
    - : AcceptedByOriginator
    - : UpMod
    - : DownMod
    - : Offensive
    - : Favourite (if VoteTypeId = 5 UserId will be populated)
    - : Close
    - : Reopen
    - : BountyStart
    - : BountyClose
    - : Deletion
    - : Undeletion
    - : Spam
    - : InformModerator

* UserId (only for VoteTypeId 5)
* CreationDate

The CSV file contains 5 columns. The first column is the Id of a vote, the second column is 
the Id of a post, the third column is the type of a vote (such as favourite), the fourth 
column has a value only if it is a favourite vote, and the fifth column is the creation time 
of a vote. 

Your task is to **find the Ids of all posts that are favoured by more than three users. Your 
output should only contain PostIds, sorted in descending order according to their NUMERIC 
values.**

The solution is already given in the file "findpost.py. In this task, we read data from and 
write data to the local file system, rather than HDFS. 

In the CSV file, the columns are separated by ",", and thus we can use the split(",") 
function to get the 5 columns from each line. Then, we use the filter() operation to obtain 
the posts that have VoteTypeId 5.

Next, for each post, we need to compute the number of users who have favoured it. Since each 
user can only favour a post once, this step is similar to the word count task. After computing 
the number of users for each post, we next apply the filter() operation to this RDD to store 
the posts which have been favoured by more than 3 users.

The last step is to sort the results. We can use sortByKey() to do the sorting, and then the 
map() operation throws away the count of users.

Use the following command to run the program:
`spark-submit findpost.py`

You can see the result in the file /home/output/part-00000 as:

```
313
266
155
```