# Try it: using CSV data
Consider the same CSV file as last slide. Suppose you want a list of distinct salaries and, for each of those salaries, 
the last names of employees on that salary. Try writing a MRJob job that will do that for you.

When you click the panel on the right you will get a terminal connection to a server that has Hadoop and YARN installed 
and running, and has the file "employees.csv" in your home directory in the local file system. Here are the fields in 
the file again:

```
employee_id (integer)
first_name (string)
last_name (string)
email (string)
phone_number (string)
hire_date (date)
salary (integer)
```

A file job.py has been started for you. Your task is to finish writing that file.

You can test your job by running the following command:

`python job.py employees.csv`
