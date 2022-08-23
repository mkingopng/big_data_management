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


class Job(MRJob):

    def mapper(self, _, line):

        ts, text = line.split(',')
        year = ts[:4]
        terms = text.split()
        for w in terms:
            yield w, (year, 1)

    def reducer(self, term, year_count_pairs):
        year_count = {}
        for year, count in year_count_pairs:
            if year not in year_count:
                year_count[year] = count
            else:
                year_count[year] += count

        max_year_count_pair = sorted(year_count.items(), key=lambda x: (x[1], x[0]))[-1]
        year = max_year_count_pair[0]
        count = max_year_count_pair[1]
        yield term, f"{year}:{count}"


if __name__ == '__main__':
    Job.run()

# test locally: python 4a.py abcnews.txt

# create a default directory on hdfs
# hdfs dfs -mkdir -p /user/user

# copy the file to it
# hdfs dfs -put abcnews.txt

# pass this file to job.py and store the output in hdfs
# python job.py -r hadoop hdfs:///user/user/abcnews.txt -o hdfs:///user/user/output

# check the results on hdfs
# hdfs dfs -cat output/p*
