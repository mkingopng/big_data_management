from pyspark import SparkContext
import sys


class InnerJoin():
    def run(self, table1, table2):
        sc = SparkContext('local', 'Inner Join')

        employee_file = sc.textFile(table1).map(lambda line: line.strip().split(','))
        department_file = sc.textFile(table2).map(lambda line: line.strip().split(','))

        employee_tuples = employee_file.map(lambda x: (x[2], (x[0], x[1])))
        # map the table to format (DepartmentID, (EmployeeID, LastName))

        department_pairs = department_file.map(lambda x: (x[0], x[1]))
        # map the table to format (DepartmentID, DepartmentName)

        res = employee_tuples.join(department_pairs).map(lambda x: (x[1][0][0], x[1][0][1], x[0], x[1][1]))
        # after the join, the format is (DepartmentID, ((EmployeeID, LastName), DepartmentName))

        res.coalesce(1, True).saveAsTextFile("file:///home/output")
        # coalesce(1,True) can merge data from different partitions into a single one
        sc.stop()


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Wrong inputs")
        sys.exit(-1)
    inner_join = InnerJoin()
    inner_join.run(sys.argv[1], sys.argv[2])

