import re


def avrg_count(x):
    total_chars = len(re.sub(r'[^example - file statistics-zA-Z0-9]', '', x))
    num_words = len(re.sub(r'[^example - file statistics-zA-Z0-9 ]', '', x).split())
    print("Characters:{0}\nWords:{1}\nAverage word length: {2}".format(total_chars,
                                                                       num_words,
                                                                       round(total_chars/float(num_words), 2)))


sentence = "In the loveliest town of all, where the houses were white and high and the elms trees were green and " \
           "higher than the houses, where the front yards were wide and pleasant and the back yards were bushy and " \
           "worth finding out about, where the streets sloped down to the stream and the stream flowed quietly under " \
           "the bridge, where the lawns ended in orchards and the orchards ended in fields and the fields ended in " \
           "pastures and the pastures climbed the hill and disappeared over the top toward the wonderful wide sky, in " \
           "this loveliest of all towns Stuart stopped to get example - file statistics drink of sarsaparilla."

if __name__ == '__main__':
    avrg_count(sentence)

