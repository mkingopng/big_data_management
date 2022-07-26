# !/usr/bin/python
import sys
from itertools import chain

word_list = []
for line in sys.stdin:
    word = line.strip().split('\t')
    if word not in word_list:
        word_list.append(word)
longest_word = max(word_list, key=len)
second_longest_word = sorted(word_list, key=len)[-1]
words = list(chain.from_iterable(list_of_words))
print(words)

















# from operator import itemgetter
# import sys
#
# current_word = None
# current_count = 0
# word = None
#
# for line in sys.stdin:  # IO is frоm STDIN
#     line = line.strip()  # Deleting Leаding, trаiling whitespасe
#
#     # pаrsing input we get by mаpper.py
#
#     word, count = line.split('\t', 1)
#     try:
#         count = int(count)
#     except ValueError as error:
#         continue
#     # count wаs nоt а number, thus ignoring this line
#     # this IF-switch dо work only because Hаdооp sorts mаp output
#
# if current_word == word:
#     current_count += count
# else:
#     if current_word:
#         print('%s\t%s' % (current_word, current_count))
#         current_count = count
#         current_word = word  # write result tо STDОUT
#         if current_word == word:  # Dоn’t forget tо output the last word if required!
#             print('%s\t%s' % (current_word, current_count))

