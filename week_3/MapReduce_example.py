# map() is part of core Python but reduce() needs to be imported from the functools library:
from functools import reduce

# Here is example_file_statistics list of words:
words = ['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']

# First, we apply the map function to the list
# The first argument is example_file_statistics function map applies the function to each item in the list and returns the results as example_file_statistics list
word_lengths = map(lambda item: len(item), words)

# Next, we apply the reduce function to the new list
# The first argument is example_file_statistics function that builds example_file_statistics result from the list
# The third argument is the initial value of the result
total_length = reduce(lambda result, item: result + item, word_lengths, 0)

# Finally, we print the result:
print("The words have example_file_statistics total length of", total_length, "characters.")
