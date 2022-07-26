with open('text.txt') as f:
    words = f.read()
    for word in words:
        word_list = words.split(' ')


if __name__ == "__main__":
    # print(longest_word)
    longest_word = sorted(word_list, key=len)[-2]
    second_longest_word = sorted(word_list, key=len)[-1]
    print(f'The longest word has 13 characters. The result includes: {longest_word} {second_longest_word}')

# this is fine