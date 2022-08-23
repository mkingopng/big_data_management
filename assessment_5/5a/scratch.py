"""
this now works for the first part. I get the right dictionaries printing.
I think i need to turn it into an iterable, such as a list of dictionaries, to
make the aggregation work
"""

abc_news = 'abcnews.txt'
stop_words = 'stopwords.txt'

# def mapper(line):
with open(abc_news) as file:
    while line := file.readline().rstrip():
        ts, text = line.split(',')
        year = ts[:4]
        words = text.split()
        filtered_words = []
        for word in words:
            if word not in stop_words:
                filtered_words.append(word)
                word_count_pairs = {}
                wcp = []
                for word in filtered_words:
                    word_count_pairs[year] = (word, 1)
                    print(word_count_pairs)
                    wcp.append(word_count_pairs)
                print(wcp)

            # word_count = {}
            # for word, count in word_count_pairs:
            #      if word not in word_count:
            #          word_count[word] = count
            #      else:
            #          word_count[word] += count
            # max_word_count_pair = sorted(word_count.items(), key=lambda x: (x[1], x[0]))[-1]
            # word = max_word_count_pair[0]
            # count = max_word_count_pair[1]
            # print(year, f'{word}: {count}')