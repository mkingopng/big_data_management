#!/usr/bin/python
import sys

res_dict = {}

for line in sys.stdin:
    index, value = line.strip().split('\t')
    res_dict[index] = res_dict.get(index,[])+[value]

print(res_dict)

