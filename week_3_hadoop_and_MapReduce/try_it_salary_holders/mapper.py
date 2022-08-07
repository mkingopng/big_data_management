#!/usr/bin/python
import sys
for line in sys.stdin:
    fields = line.strip().split(',')
    last_name = fields[2]
    salary = fields[-1]
    print(salary, '\t', last_name)