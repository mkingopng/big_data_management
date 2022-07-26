#!/usr/bin/python
import sys
max_salary = 0
for line in sys.stdin:
    fields = line.strip().split(',')
    max_salary = max(max_salary, int(fields[-1]))
print('max_salary', '\t', max_salary)