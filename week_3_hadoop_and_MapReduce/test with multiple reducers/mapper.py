#!/usr/bin/python
import sys
for line in sys.stdin:
    fields = line.strip().split(',')
    # Previous output
    # print('salary', '\t', fields[-1])
    print(fields[-1])