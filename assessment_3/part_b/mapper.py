#!/usr/bin/python
import sys
for line in sys.stdin:
    fields = line.strip().split(',')
    print('salary', '\t', fields[-1])