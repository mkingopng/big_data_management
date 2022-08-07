# Part B - MRJob with CSV (4 marks)
In Part B your task is to answer a question about the data in a CSV file using MRJob. When you click the panel on the 
right you'll get a connection to a server that has, in your home directory, a CSV file called "orders.csv", containing 
data about book orders (feel free to open the file and explore its contents). 

Here are the fields in the file:

```
OrderDate (date)
ISBN (string)
Title (string)
Category (string)
PriceEach (decimal(5,2))
Quantity (integer)
FirstName (string)
LastName (string)
City (string)
```

Your task is to compute the average cost of books per customer, i.e., the total spent for books of a customer divided 
by the number of books purchased by the customer.

The result should be rounded to two decimal places, with round(x,2), as shown below (MRJob output):

```
"BECCA NELSON"    34.18
"BONITA MORALES"    36.55
"CINDY GIRARD"    20.63
"GREG MONTIASA"    30.98
"JAKE LUCAS"    70.62
"JASMINE LEE"    55.95
"JENNIFER SMITH"    55.95
"KENNETH FALAH"    66.62
"KENNETH JONES"    19.95
"LEILA SMITH"    72.22
"REESE MCGOVERN"    55.95
"STEVE SCHELL"    8.95
"TAMMY GIANA"    48.91
"THOMAS PIERSON"    19.95
```

Write an MRJob job to do this. A file called "job.py" has been created for you - you just need to fill in the details. 
**Note that you are required to implement a combiner to do this task.**

You can test your job locally by running the following command (it tells Python to execute job.py locally, using 
orders.csv as the input):

`python job.py orders.csv`

To run your code on Hadoop, you can use the following command (the results would be sorted by keys as you can see in 
"output"):

`python job.py orders.csv -r hadoop > output`

