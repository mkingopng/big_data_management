#!/usr/bin/python
import sys
salary = []
number_of_employees = []
for line in sys.stdin:
    index, value = line.split('\t')
    if line[6] is int:
        number_of_employees += 1
        salary.append(line[6])
        total_salary = sum(salary)
        number_of_employees = sum(number_of_employees)
        avg_salary = total_salary / number_of_employees
        print(salary)