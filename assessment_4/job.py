"""
compute for each term, in which year it appears the most. That is, for each term, you count how many
articles contain this word in each year, and then select the year that has the most articles with this term (note
that if an article contains a term multiple times, it only contributes 1 to the frequency). If the term appears in
several years with the same frequency, select the earliest year as the result.

In your output, each line contains a key-value pair, where the key is the term, and the value is a pair of the year
and this term's frequency in this year. For example, given the above data set, the output should be (there is no
need to remove the quotation marks):
"""

from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")


class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield word.lower(), 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)


if __name__ == '__main__':
    MRWordFreqCount.run()
