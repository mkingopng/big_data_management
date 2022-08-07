# Working with CSV
In the word frequency example, we worked with a text file. Now let's try working with a CSV file.

When you click the panel on the right you will get a terminal connection to a server that has, in your home directory 
on this server, a CSV file called "employees.csv". You can open the file to inspect its contents. The fields in the file 
are as follows:
```
employee_id (integer)
first_name (string)
last_name (string)
email (string)
phone_number (string)
hire_date (date)
salary (integer)
```

## Maximum salary
Suppose we want to know the maximum salary of employees. How might we do it using a mapper and reducer? The mapper is 
applied to only part of the file, so it cannot calculate the overall maximum salary. But it can return each of the 
salaries, and then we can get the reducer find the maximum of those salaries.

On the server you will see files called "mapper.py" and "reducer.py" - these are mappers and reducers written in Python 
which will do what we want.

You can see the results by running the following command:

```$ python mapper.py < employees.csv | python reducer.py```

This command tells Python to execute the program mapper.py, using the file employees.csv as input, and then pipe the 
results as input to reducer.py (we use | to indicate that we want the results piped to the next process).

Once we're happy that the mapper and reducer are working correctly we could run them as a MapReduce job on Hadoop, as 
per the previous slide. But we won't do that - for the purpose of learning the concept of mapping reducing the above 
should suffice.

## An alternative method

You may have noticed that mapper.py is a bit lazy - it doesn't calculate the maximum salary among the salaries that it 
has, it just returns each salary paired with 1, and lets reducer.py do the rest.

We could write an alternative mapper which returns just a single <key, value> pair, containing the maximum salary among 
the salaries that it has. Then the reducer just needs to find the maximum values of these local maxima. This means that 
less data needs to be sent across the Hadoop cluster for the reducer to reduce.

You will also see, on the server, a Python program called mapper2.py, which does this. Try it out - you should get the 
same result:

```$ python mapper2.py < employees.csv | python reducer.py```
