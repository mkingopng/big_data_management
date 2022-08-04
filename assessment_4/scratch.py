# count-list-items-1.py

wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")  # prints the word string
print("List\n" + str(wordlist) + "\n")  # prints a list of words from the text. duplicates allowed
print("Frequencies\n" + str(wordfreq) + "\n")  # print frequencies, just returns numbers representing count. no words
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))  # print a dictionary with the count of each word

