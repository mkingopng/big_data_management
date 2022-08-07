from mrjob.job import MRJob


class Job(MRJob):
    def mapper(self, key, value):
        yield "No. lines", 1
        yield "No. words", len(value.split())
        yield "No. characters", len(value)

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    Job.run()
