from mrjob.job import MRJob


class Job(MRJob):
    def mapper(self, key, value):
        fields = value.strip().split(',')
        yield int(fields[-1]), fields[2]

    def combiner(self, key, values):
        yield key, ','.join(values)

    def reducer(self, key, values):
        yield key, ','.join(values)


if __name__ == '__main__':
    Job.run()
