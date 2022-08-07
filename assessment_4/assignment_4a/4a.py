from mrjob.job import MRJob


class Job(MRJob):
    def mapper(self, key, value):
        fields = value.strip().split(',')
        # select the first 4 numbers for the year
        date = fields[0]
        for char in date:
            year = date[0:4]
            yield year, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    Job.run()

#

# test locally: python 4a.py abcnews.txt
