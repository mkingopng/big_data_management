# Example: using CSV data
Now let's try working with a CSV file.

When you click the panel on the right you will get a terminal connection to a server that has Hadoop and YARN installed.

In your home directory on this server is a CSV file called "employees.csv". You can open the file to inspect its 
contents. The fields in the file are as follows:

```
employee_id (integer)
first_name (string)
last_name (string)
email (string)
phone_number (string)
hire_date (date)
salary (integer)
```

Suppose we want to know the maximum salary of employees. Let's write a MRJob program to calculate it.

## Without a combiner
The mapper is applied to only part of the file, so it cannot calculate the overall maximum salary. But it can return 
each of the salaries, and then let the reducer find the maximum of salaries.

The program "job1.py" does this. You can run the program using employees.csv as the input using the following command:

`python job1.py employees.csv`

## With a combiner
You may have noticed that mapper() is a bit lazy - it doesn't calculate the maximum salary among the salaries that it 
has, it just returns each salary paired with 1, and lets reducer() do the rest.

We can do better, by adding a combiner, which first finds the local maximum salary before the results get sent to the 
reducer.

The program "job2.py" does this. You can run the program using employees.csv as the input using the following command:

`python job2.py employees.csv`
