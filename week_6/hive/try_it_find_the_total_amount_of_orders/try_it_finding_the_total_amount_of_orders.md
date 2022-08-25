# Try it: find the total amount of orders
When you click the panel on the right you'll get a connection to a server that 
has, in your home directory, a CSV file called "orders.csv", containing data 
about book orders (feel free to open the file and explore its contents). 

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

Your task is to find the total dollar amount of orders for each city.

Your results should appear as the following:

```
ATLANTA        211.85
AUSTIN         391.25
BOISE          39.9
CHEYENNE       19.95
CHICAGO        111.9
CODY           55.95
EASTPOINT      182.75
KALMAZOO       170.9
MACON          61.95
MIAMI          17.9
MORRISTOWN     55.95
SEATTLE        61.9
TALLAHASSEE    144.45
TRENTON        199.85
```

Write a Hive script to do this. A file called "script.hql" has been created for 
you - you just need to fill in the details. You should be able to modify Hive 
scripts that you have already seen in this week's content. 

You can test your script by running the following command (it tells Hive to 
execute the commands contained in the file script.hql):

> $ hive -f script.hql
 