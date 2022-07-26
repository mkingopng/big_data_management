import sys
results = {}
for line in sys.stdin:
    for word in line.strip().split():
        results[word] = results.get(word, 0) + 1
words = list(results.keys())
words.sort()
for word in words:
    print(word, results[word])
