# https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2799933550853697/1880776780418274/2202577924924539/latest.html

# read the txt file
# 'dbfs:/FileStore/shared_uploads/michaelkennethkingston@gmail.com/shakespeare.txt'

from pyspark.sql import SparkSession

sc = SparkSession

# **Part 1: Creating a base RDD and pair RDDs** 

# In this part of the lab, we will explore creating a base RDD with parallelize
# and using pair RDDs to count words.

# (1a) Create a base RDD We'll start by generating a base RDD by using a Python
# list and the sc.parallelize method. Then we'll print out the type of the base
# RDD.

wordsList = ['cat', 'elephant', 'rat', 'rat', 'cat']
wordsRDD = sc.parallelize(wordsList, 4)

# Print out the type of wordsRDD
print(type(wordsRDD))


# **(1b) Pluralize and test**

# Let's use a `map()` transformation to add the letter 's' to each string in
# the base RDD we just created. We'll define a Python function that returns
# the word with an 's' at the end of the word. Please replace ``<FILL IN>``
# with your solution. If you have trouble, the next cell has the solution.
# After you have defined `makePlural` you can run the third cell which contains
# a test. If you implementation is correct it will print `1 test passed`.

# This is the general form that exercises will take, except that no solution
# will be provided. Exercises will include an explanation of what is expected,
# followed by code cells where one cell will have one or more `<FILL IN>`
# sections. The cell that needs to be modified will have
# TODO: Replace <FILL IN> with appropriate code` on its first line. Once the
#  `<FILL IN>` sections are updated and the code is run, the test cell can then
#  be run to verify the correctness of your solution. The last code cell before
#  the next markdown section will contain the tests.

# TODO: Replace <FILL IN> with appropriate code
def makePlural(word):
    """
    Adds an 's' to `word`.
    Note: This is a simple function that only adds an 's'.  No attempt is made
    to follow proper pluralization rules.

    Args: word (str): A string.
    Returns: str: A string with 's' added to it.
    """
    # return <FILL IN>
    return word + 's'


print(makePlural('cat'))


# One way of completing the function
def makePlural(word):
    return word + 's'


print(makePlural('cat'))

# **WARNING**: If test_helper, required in the cell below, is not installed,
# follow the instructions here.

# Load in the testing code and check to see if your answer is correct
# If incorrect it will report back '1 test failed' for each failed test

# Make sure to rerun any cell you change before trying the test again
from test_helper import Test

# TEST Pluralize and test (1b)
Test.assertEquals(makePlural('rat'), 'rats',
                  'incorrect result: makePlural does not add an s')

# TODO: Replace <FILL IN> with appropriate code
# pluralRDD = wordsRDD.map(<FILL IN>)

pluralRDD = wordsRDD.map(makePlural)
print(pluralRDD.collect())

# TEST Apply makePlural to the base RDD(1c)
Test.assertEquals(pluralRDD.collect(),
                  ['cats', 'elephants', 'rats', 'rats', 'cats'],
                  'incorrect values for pluralRDD')

# **(1d) Pass a `lambda function()` to `map()`**
# Let's create the same RDD using a lambda function.

# TODO: Replace <FILL IN> with appropriate code
# pluralLambdaRDD = wordsRDD.map(lambda <FILL IN>)
pluralLambdaRDD = wordsRDD.map(lambda x: makePlural(x))
print(pluralLambdaRDD.collect())

# TEST Pass a lambda function to map (1d)
Test.assertEquals(pluralLambdaRDD.collect(),
                  ['cats', 'elephants', 'rats', 'rats', 'cats'],
                  'incorrect values for pluralLambdaRDD (1d)')

# **(1e) Length of each word**
# Now use `map()` and a `lambda()` function to return the number of characters
# in each word. We'll collect this result directly into a variable.

# TODO: Replace <FILL IN> with appropriate code
# pluralLengths = (pluralRDD <FILL IN>.collect())
pluralLengths = (pluralRDD
                 .map(lambda x: len(x))
                 .collect())

print(pluralLengths)

# TEST Length of each word (1e)
Test.assertEquals(pluralLengths, [4, 9, 4, 4, 4],
                  'incorrect values for pluralLengths')

# **(1f) Pair RDDs**
# The next step in writing our word counting program is to create a new type of
# RDD, called a pair RDD. A pair RDD is an RDD where each element is a pair
# tuple `(k, v)` where `k` is the key and `v` is the value. In this example,
# we will create a pair consisting of `('<word>', 1)` for each word element
# in the RDD. We can create the pair RDD using the `map()` transformation with
# a `lambda()` function to create a new RDD.

# TODO: Replace <FILL IN> with appropriate code
# wordPairs = wordsRDD.<FILL IN>

wordPairs = wordsRDD.map(lambda x: (x, 1))
print(wordPairs.collect())

# TEST Pair RDDs (1f)
Test.assertEquals(wordPairs.collect(),
                  [('cat', 1), ('elephant', 1), ('rat', 1), ('rat', 1),
                   ('cat', 1)],
                  'incorrect value for wordPairs')

# **Part 2: Counting with pair RDDs**

# Now, let's count the number of times a particular word appears in the RDD.
# There are multiple ways to perform the counting, but some are much less
# efficient than others. A naive approach would be to `collect()` all the
# elements and count them in the driver program. While this approach could work
# for small datasets, we want an approach that will work for any size dataset
# including terabyte- or petabyte-sized datasets. In addition, performing all
# the work in the driver program is slower than performing it in parallel in
# the workers. For these reasons, we will use data parallel operations.

# **(2a) groupByKey() approach**
# An approach you might first consider (we'll see shortly that there are better
# ways) is based on using the `groupByKey()` transformation. As the name
# implies, the `groupByKey()` transformation groups all the elements of the
# RDD with the same key into a single list in one of the partitions.

# There are two problems with using `groupByKey()`:
# - The operation requires a lot of data movement to move all the values into
# the appropriate partitions. The lists can be very large. Consider a word
# count of English Wikipedia: the lists for common words (e.g., the, a, etc.)
# would be huge and could exhaust the available memory in a worker.

# Use `groupByKey()` to generate a pair RDD of type `('word', iterator)`.

# TODO: Replace <FILL IN> with appropriate code
# Note that groupByKey requires no parameters
# wordsGrouped = wordPairs.<FILL IN>

wordsGrouped = wordPairs.groupByKey()
for key, value in wordsGrouped.collect():
    print('{0}: {1}'.format(key, list(value)))

# TEST groupByKey() approach (2a)
Test.assertEquals(sorted(wordsGrouped.mapValues(lambda x: list(x)).collect()),
                  [('cat', [1, 1]), ('elephant', [1]), ('rat', [1, 1])],
                  'incorrect value for wordsGrouped')

# **(2b) Use groupByKey() to obtain the counts**
# Using the `groupByKey()` transformation creates an RDD containing 3 elements,
# each of which is a pair of a word and a Python iterator.

# Now sum the iterator using a `map()` transformation. The result should be a
# pair RDD consisting of (word, count) pairs.


# TODO: Replace <FILL IN> with appropriate code
# wordCountsGrouped = wordsGrouped.<FILL IN>

# Option 1: problem
# wordCountsGrouped = wordsGrouped.map(lambda k, v: (k, len(v)))

# Option 2
wordCountsGrouped = wordsGrouped.map(lambda x: (x[0], len(x[1])))
print(wordCountsGrouped.collect())

# TEST Use groupByKey() to obtain the counts (2b)
Test.assertEquals(sorted(wordCountsGrouped.collect()),
                  [('cat', 2), ('elephant', 1), ('rat', 2)],
                  'incorrect value for wordCountsGrouped')

# **(2c) Counting using reduceByKey**
# A better approach is to start from the pair RDD and then use the
# `reduceByKey()` transformation to create a new pair RDD. The `reduceByKey()`
# transformation gathers together pairs that have the same key and applies the
# function provided to two values at a time, iteratively reducing all the
# values to a single value. `reduceByKey()` operates by applying the function
# first within each partition on a per-key basis and then across the
# partitions, allowing it to scale efficiently to large datasets.

from operator import add

# TODO: Replace <FILL IN> with appropriate code
# Note that reduceByKey takes in a function that accepts two values and returns
# a single value

# wordCounts = wordPairs.reduceByKey(<FILL IN>)

# Option 1
# wordCounts = wordPairs.reduceByKey(lambda x, y: x + y)

# Option 2: this one is faster
wordCounts = wordPairs.reduceByKey(add)
print(wordCounts.collect())

# TEST Counting using reduceByKey (2c)
Test.assertEquals(sorted(wordCounts.collect()),
                  [('cat', 2), ('elephant', 1), ('rat', 2)],
                  'incorrect value for wordCounts')

# **(2d) All together**

# The expert version of the code performs the `map()` to pair RDD,
# `reduceByKey()` transformation, and `collect` in one statement.

# TODO: Replace <FILL IN> with appropriate code
# wordCountsCollected = (wordsRDD
#                        <FILL IN>
#                        .collect())

wordCountsCollected = (wordsRDD
                       .map(lambda x: (x, 1))
                       .reduceByKey(add)
                       .collect())

print(wordCountsCollected)

# TEST All together (2d)
Test.assertEquals(sorted(wordCountsCollected),
                  [('cat', 2), ('elephant', 1), ('rat', 2)],
                  'incorrect value for wordCountsCollected')

# **Part 3: Finding unique words and a mean value**
# **(3a) Unique words**
# Calculate the number of unique words in wordsRDD. You can use other RDDs that
# you have already created to make this easier.

# TODO: Replace <FILL IN> with appropriate code
# uniqueWords = <FILL IN>

uniqueWords = wordCounts.count()
print(uniqueWords)

# TEST Unique words (3a)
Test.assertEquals(uniqueWords, 3, 'incorrect count of uniqueWords')

# **(3b) Mean using reduce**
# Find the mean number of words per unique word in wordCounts.
# Use a `reduce()` action to sum the counts in wordCounts and then divide by
# the number of unique words. First `map()` the pair RDD wordCounts, which
# consists of (key, value) pairs, to an RDD of values.

# TODO: Replace <FILL IN> with appropriate code

from operator import add

# totalCount = (wordCounts
#               .map(<FILL IN>)
#               .reduce(<FILL IN>))
# average = totalCount / float(<FILL IN>)

totalCount = (wordCounts
              .map(lambda k, v: v)
              .reduce(add))
average = totalCount / float(wordCounts.count())
print(totalCount)
print(round(average, 2))

# TEST Mean using reduce (3b)
Test.assertEquals(round(average, 2), 1.67, 'incorrect value of average')


# **Part 4: Apply word count to a file**
# In this section we will finish developing our word count application. We'll
# have to build the wordCount function, deal with real world problems like
# capitalization and punctuation, load in our data source, and compute the word
# count on the new data.

# **(4a) wordCount function**

# First, define a function for word counting. You should reuse the techniques
# that have been covered in earlier parts of this lab. This function should
# take in an RDD that is a list of words like wordsRDD and return a pair RDD
# that has all the words and their associated counts.


# TODO: Replace <FILL IN> with appropriate code
def wordCount(wordListRDD):
    """
    Creates a pair RDD with word counts from an RDD of words.
    Args: wordListRDD (RDD of str): An RDD consisting of words.
    Returns: RDD of (str, int): An RDD consisting of (word, count) tuples.
    """
    #    <FILL IN>
    return wordListRDD.map(lambda s: (s, 1)).reduceByKey(add)


print(wordCount(wordsRDD).collect())

# TEST wordCount function (4a)
Test.assertEquals(sorted(wordCount(wordsRDD).collect()),
                  [('cat', 2), ('elephant', 1), ('rat', 2)],
                  'incorrect definition for wordCount function')

# **Regular expressions 101**
# A regular expression (regex or regexp for short) is a special text string for
# describing a search pattern. A simple way of thinking of regular expressions
# is as wildcards on steroids; you may be familiar with wildcard notations such
# as *.txt to find all text files in a file manager.

# They are very useful to find and collect a specific type of pattern in a
# given string.

# Python supports regular expressions through the re module. As you might have
# guessed by now this can be imported with:

import re

# In Python a regular expression search is typically written as:
# **match = re.search(pat, str)**
# Here is a very simple of example of how to use regular expressions in Python

# These are the patterns you are looking for
patterns = ['this', 'that', 'these', 'those']

# This is the string where you want to find the given paters
text = 'Does this text match the pattern? , What about those?'

# A nice and simple loop to find your patters in the given text
for pattern in patterns:
    print('Looking for "%s" in "%s" ->' % (pattern, text)),

    if re.search(pattern, text):
        print('found a match!')
    else:
        print('no match')

# There are many resources to get familiar with regex and we encourage you to
# vist them. Here are some suggestions:

# https://docs.python.org/2/library/re.html

# http://regexone.com/references/python

# https://developers.google.com/edu/python/regular-expressions

# The following website is particularly useful as it allows you to test your
# regex online

# https://regex101.com/#python

# Finally, a very useful book on regex

# Hint. For this lab you may want to check the following resource in order to
# implement the function that removes punctuation
# https://docs.python.org/2/library/re.html#re.sub

# **(4b) Capitalization and punctuation**
# Real world files are more complicated than the data we have been using in
# this lab. Some of the issues we have to address are:

# - Words should be counted independent of their capitialization (e.g., Spark
# and spark should be counted as the same word).
# - All punctuation should be removed.
# - Any leading or trailing spaces on a line should be removed.

# Define the function `removePunctuation` that converts all text to lower case,
# removes any punctuation, and removes leading and trailing spaces. Use the
# Python re module to remove any text that is not a letter, number, or space.
# Reading `help(re.sub)` might be useful. If you are unfamiliar with regular
# expressions, you may want to review this tutorial from Google. Also, this
# website is a great resource for debugging your regular expression.

# TODO: Replace <FILL IN> with appropriate code
import re
import string


def removePunctuation(text):
    """
    Removes punctuation, changes to lower case, and strips leading and trailing
    spaces. Note: Only spaces, letters, and numbers should be retained.  Other
    characters should be eliminated (e.g. it's becomes its).  Leading
    and trailing spaces should be removed after punctuation is removed.
    Args: text (str): A string.
    Returns: str: The cleaned up string.
    """
    no_puntuation = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    lowercase = no_puntuation.lower()
    trimmed = lowercase.strip()
    return trimmed

    # solution 2
    #     lowercase = text.lower()
    #     no_puntuation = re.sub(r'[^a-z0-9\s]','', lowercase)
    #     strip = no_puntuation.strip()
    # return strip


print(removePunctuation('Hi, you!'))
print(removePunctuation(' No under_score!'))
print(removePunctuation(' *      Remove punctuation then spaces  * '))

# TEST Capitalization and punctuation (4b)
Test.assertEquals(removePunctuation(" The Elephant's 4 cats. "),
                  'the elephants 4 cats',
                  'incorrect definition for removePunctuation function')

# (4c) Load a text file
# For the next part of this lab, we will use the Complete Works of William
# Shakespeare from Project Gutenberg. To convert a text file into an RDD, we
# use the `SparkContext.textFile()` method. We also apply the recently defined
# `removePunctuation()` function using a `map()` transformation to strip out
# the punctuation and change all text to lower case. Since the file is large we
# use `take(15)`, so that we only print 15 lines.

# Just run this code
fileName = 'shakespeare.txt'

shakespeareRDD = (sc
                  .textFile(fileName, 8)
                  .map(removePunctuation))
print('\n'.join(shakespeareRDD
                .zipWithIndex()  # to (line, lineNum)
                .map(
    lambda l, num: '{0}: {1}'.format(num, l))  # to 'lineNum: line'
                .take(15)))

# **(4d) Words from lines**
# Before we can use the wordcount() function, we have to address two issues
# with the format of the RDD:
# - The first issue is that we need to split each line by its spaces.
# Performed in (4d).
# - The second issue is we need to filter out empty lines. Performed in (4e).

# Apply a transformation that will split each element of the RDD by its spaces.
# For each element of the RDD, you should apply Python's string split()
# function. You might think that a map() transformation is the way to do this,
# but think about what the result of the split() function will be.

# Note: Do not use the default implemenation of split(), but pass in a
# separator value. For example, to split line by commas you would use
# line.split(',').

# TODO: Replace <FILL IN> with appropriate code
# shakespeareWordsRDD = shakespeareRDD.<FILL_IN>

shakespeareWordsRDD = shakespeareRDD.flatMap(lambda x: x.split())
shakespeareWordCount = shakespeareWordsRDD.count()
print(shakespeareWordsRDD.top(5))
print(shakespeareWordCount)

# TEST Words from lines (4d)
# This test allows for leading spaces to be removed either before or after
# punctuation is removed.

Test.assertTrue(
    shakespeareWordCount == 927631 or shakespeareWordCount == 928908,
    'incorrect value for shakespeareWordCount')
Test.assertEquals(shakespeareWordsRDD.top(5),
                  [u'zwaggerd', u'zounds', u'zounds', u'zounds', u'zounds'],
                  'incorrect value for shakespeareWordsRDD')

# (4e) Remove empty elements
# The next step is to filter out the empty elements. Remove all entries where
# the word is ''.

# TODO: Replace <FILL IN> with appropriate code
# shakeWordsRDD = shakespeareWordsRDD.<FILL_IN>

# option 1
# shakeWordsRDD = shakespeareWordsRDD.filter(lambda x: x != '')

# option 2
shakeWordsRDD = shakespeareWordsRDD.filter(lambda s: len(s) > 0)

shakeWordCount = shakeWordsRDD.count()
print(shakeWordCount)

# TEST Remove empty elements (4e)
Test.assertEquals(shakeWordCount, 882996, 'incorrect value for shakeWordCount')

# (4f) Count the words
# We now have an RDD that is only words. Next, let's apply the `wordCount()`
# function to produce a list of word counts. We can view the top 15 words by
# using the `takeOrdered()` action; however, since the elements of the RDD are
# pairs, we need a custom sort function that sorts using the value part of the
# pair.

# You'll notice that many of the words are common English words. These are
# called stopwords. In a later lab, we will see how to eliminate them from the
# results. Use the `wordCount()` function and `takeOrdered()` to obtain the
# fifteen most common words and their counts.

# TODO: Replace <FILL IN> with appropriate code
# top15WordsAndCounts = <FILL IN>
top15WordsAndCounts = wordCount(shakeWordsRDD).takeOrdered(15, key=lambda k, v: -v)
print('\n'.join(map(lambda w, c: '{0}: {1}'.format(w, c), top15WordsAndCounts)))

# TEST Count the words (4f)
Test.assertEquals(top15WordsAndCounts,
                  [(u'the', 27361), (u'and', 26028), (u'i', 20681),
                   (u'to', 19150), (u'of', 17463),
                   (u'a', 14593), (u'you', 13615), (u'my', 12481),
                   (u'in', 10956), (u'that', 10890),
                   (u'is', 9134), (u'not', 8497), (u'with', 7771),
                   (u'me', 7769), (u'it', 7678)],
                  'incorrect value for top15WordsAndCounts')

# **Download stops words**

get_ipython().system('wget http://tacit.usc.edu/resources/stopwords_eng.txt')

# copy to a directory, This solution is not recommended for large jobs since we
# are copying the file directly to the driver!
localpath = "file:/databricks/driver/stopwords_eng.txt"

sw = sc.textFile(localpath)

sw.take(10)

# Remove stop words
# At this point we have process the full text and found stops words are the
# most frequent words. Remove stop words, after, find the top 20 words from the
# Complete Works of William Shakespeare.

# Interpret your results. What can you infer?

# Option 1
sw_collected = sw.collect()
no_stop_words_shakeWordsRDD = (shakeWordsRDD
                               .map(lambda x: (x, 1))
                               .reduceByKey(add)
                               .filter(lambda k, v: k not in sw_collected)
                               )

no_stop_words_shakeWordsRDD.take(10)

no_stop_words_shakeWordsRDD.takeOrdered(20, key=lambda k, v: -v)

# Option 2
# broadcast stopwords to all executors so they're not sent
# with every transformation or action they're referenced

bsw = sc.broadcast(sw.collect())

noStopWordsRDD = (shakeWordsRDD.filter(lambda s: s not in bsw.value))

(wordCount(noStopWordsRDD).takeOrdered(20, key=lambda k, v: -v))

shakeWordsRDD.getNumPartitions()
