from mrjob.job import MRJob


class Job(MRJob):
    def mapper(self, key, value):
        for word in value.strip().split():
            yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    Job.run()
