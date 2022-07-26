#!/usr/bin/python
import sys
max_salary = 0
for line in sys.stdin:
    index, value = line.split('\t')
    max_salary = max(max_salary, int(value))
print('The maximum salary is $', max_salary)
