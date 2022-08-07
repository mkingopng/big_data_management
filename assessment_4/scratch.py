import pandas as pd

# create unique word list
word_list = []

with open('assignment_4a/abcnews.txt') as f:
    lines = f.readlines()
    for line in lines:
        date = line.split(',')[0]
        date_list = []
        date_list.append(date_list)
    for line in lines:
        words = line.strip().split(',')[1].split(' ')
        for word in words:
            if word in word_list:
                pass
            else:
                word_list.append(word)

word_dict = dict.fromkeys(word_list, 0)

word_count_df = pd.DataFrame.from_dict(word_dict, orient='index')

# print(len(word_list))  # 40 words?
# print(word_dict)
# print(word_count_df)

# count the unique words
with open('assignment_4a/abcnews.txt') as f:
    lines = f.readlines()
    for line in lines:
        words = line.strip().split(',')[1].split(' ')
        for word in line:
            if word in word_dict:
                word_dict[word] += 1
            else:
                pass

print(word_dict)


