#!/usr/bin/python
import sys
results = {}
for line in sys.stdin:
    word, frequency = line.strip().split('\t', 1)
    results[word] = results.get(word, 0) + int(frequency)
words = list(results.keys())
words.sort()
for word in words:
    print(word, results[word])