"""
for each term, you count how many articles contain this word in each year, and then select the year that has the
most articles with this term

- if an article contains a term multiple times, it only contributes 1 to the frequency.
- If the term appears in several years with the same frequency, select the earliest year as the result.

In your output, each line contains a key-value pair, where the key is the term, and the value is a pair of the year
and this term's frequency in this year.

    - key: term
    - value: a pair of year and frequency
    - desired output = word, (year, max frequency)
    - intermediate output 1 = word, (year, frequency)
    - intermediate output 2 = (word, year)

steps:
    - identify unique words
    - identify each year
    - count how many articles contain this word in each year
    - select the year that has the most articles with this term

"""
from mrjob.job import MRJob
from mrjob.step import MRStep


class Job(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words, reducer=self.reducer_count_articles_containing_each_word),
            MRStep(mapper=self.mapper_get_years, reducer=self.reducer_sort_by_year)
        ]

    def mapper_get_words(self, line, words):
        line_arr = line.strip().split(',')
        words = line_arr[1].split(' ')
        for word in words:
            yield word, 1

    def mapper_get_years(self, line, year):
        line_arr = line.strip().split(',')
        years = line_arr[0]
        for year in years:
            year = years[0:4]
            yield year, 1

    def reducer_count_articles_containing_each_word(self):
        pass

    def reducer_sort_by_year(self, year):
        pass

# test locally: python 4a.py abcnews.txt
