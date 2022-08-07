from mrjob.job import MRJob


class Job(MRJob):
    def mapper(self, _, line):
        words = line.lower().split(',')
        for word in words
            yield


    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    Job.run()
