from mrjob.job import MRJob
from collections import Counter
from itertools import chain
import re

unique_words = []
date_list = []
new_dict = {}
date_re = r'^[0-9]{8}'

text_file = open('/assessment_4/assignment_4a/abcnews.txt')
text = text_file.read()
text = text.lower()


words = text.split()  # gets rid of the new line character
words = [word.replace(",", "") for word in words]  # gets rid of the comma
for word in words:
    new_word = re.sub(pattern=date_re, repl='', string=word, count=9)
    if new_word not in unique_words:
        unique_words.append(new_word)  # and thus we end up with a list of unique words


def add_values_in_dict(new_dict, key, date, count):
    """ Append multiple values to a key in
        the given dictionary """
    if word not in new_dict:
        new_dict[key] = list(unique_words)
    new_dict[word].extend(date, count)
    return new_dict


new_dict = dict(zip(unique_words, [None] * len(unique_words)))
print(new_dict)

with open('assignment_4a/abcnews.txt') as file:
    lines = file.readlines()
    for line in lines:
        _list = line.split(',')
        new_date = _list[0]
        words = _list[1].split(' ')
        new_count = word.count(word)
        for word in words:
            for key in new_dict.keys():
                value_list = new_dict[word]
                if value_list is None or value_list < new_count:
                    new_dict = add_values_in_dict(new_dict, word, new_date, new_count)

print(new_dict)
