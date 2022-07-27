from mrjob.job import MRJob


class Job(MRJob):
    def mapper(self, key, value):
        yield value, ''

    def reducer(self, key, values):
        yield key, ''


if __name__ == '__main__':
    Job.run()
