# Try it: Inner join of two tables (CSV data)

You are given two tables which are stored in two separate files: Employee.csv and Department.csv. 
In both files, each line is split by ‘,’.  Employee.csv contains three columns:

```
EmployeeID
LastName
DepartmentID
```

Department.csv has two columns:

```
DepartmentID 
DepartmentName
```

Your task is to do the inner join over the two tables. The result should contain the following 
columns:

```
EmployeeID
LastName
DepartmentID
DepartmentName
```

The code template has been given in the file "innerjoint.py". Your program should take the two CSV 
files as the parameters. Use the following command to run the program:

`spark-submit innerjoin.py "file:///home/Employee.csv" "file:///home/Department.csv"`

Your result should be like this:

```
('0001', 'Rafferty', '31', 'Sales')
('0002', 'Jones', '33', 'Engineering')
('0003', 'Heisenberg', '33', 'Engineering')
('0004', 'Robinson', '34', 'Clerical')
('0005', 'Smith', '34', 'Clerical')
```

You need to use the RDD join() operation to do this task. 

def join[W](other: RDD[(K, W)]): RDD[(K, (V, W))]

Return an RDD containing all pairs of elements with matching keys in this and other. Each pair of 
elements will be returned as a (k, (v1, v2)) tuple, where (k, v1) is in this and (k, v2) is in 
other. Performs a hash join across the cluster.

Some examples can be found at this link: 

https://data-flair.training/forums/topic/explain-join-operation/. 