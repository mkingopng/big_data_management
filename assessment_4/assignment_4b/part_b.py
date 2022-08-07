from mrjob.job import MRJob
from statistics import mean


class Job(MRJob):

    def mapper(self, key, value):
        fields = value.strip().split(',')
        name = fields[-3] + ' ' + fields[-2]
        yield name, float(fields[4])

    def combiner(self, key, values):
        yield key, mean(values)

    def reducer(self, key, values):
        yield key, round(mean(values), 2)


if __name__ == '__main__':
    Job.run()


# cd assessment_4
# cd assignment_4b
# python part_b.py orders.csv
