from mrjob.job import MRJob


class Job(MRJob):

    def mapper(self, key, value):
        fields = value.strip().split(',')
        yield 'salary', int(fields[-1])

    def reducer(self, key, values):
        yield 'Maximum salary', max(values)


if __name__ == '__main__':
    Job.run()
