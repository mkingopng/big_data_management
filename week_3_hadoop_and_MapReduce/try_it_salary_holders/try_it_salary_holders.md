# Try it: salary holders

Now try an example yourself, using the same CSV file as the previous slide.

Suppose you want a **list of distinct salaries and, for each of those salaries, the last names of employees on that 
salary**. Try writing a mapper and reducer that will do that for you.

When you click the panel on the right you'll get a terminal connection to a server that has the file "employees.csv" in 
your home directory in the local file system. Here are the fields in the file again:

```
employee_id (integer)
first_name (string)
last_name (string)
email (string)
phone_number (string)
hire_date (date)
salary (integer)
```

Files called mapper.py and reducer.py have been started for you. Your task is to finish writing those files.

You can test your mapper and reducer by running the following command:

```$ python mapper.py < employees.csv | python reducer.py```


logic: 
- identify all the unique salaries, which will be the keys of our dictionary
- identify all the last_names related to that salary, which will be our values
- 