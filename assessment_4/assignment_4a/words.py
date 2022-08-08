from mrjob.job import MRJob


class Job(MRJob):
    def mapper(self, key, value):
        fields = value.strip().split(',')
        words = fields[1].split(' ')
        for word in words:
            yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    Job.run()

# test locally: python words.py abcnews.txt
