from mrjob.job import MRJob


class Job(MRJob):

    def mapper(self, key, value):
        for word in value.split():
            yield 'length', len(word)

    def reducer(self, key, values):
        numWords = 0
        totalLength = 0
        for value in values:
            numWords = numWords + 1
            totalLength = totalLength + value
        yield 'Average word length', totalLength/numWords


if __name__ == '__main__':
    Job.run()
