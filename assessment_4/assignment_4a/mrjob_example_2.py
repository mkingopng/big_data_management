from mrjob.job import MRJob
from mrjob.step import MRStep


class MRFemaleBirthCounter(MRJob):

    def filter_births_by_gender(self, key, record):
        if record[435] == 'F':
            year = record[14:18]
            month = record[18:20]
            birth_month = '%s-%s' % (month, year)
            yield 'Female', birth_month

    def counter_mapper(self, gender, month):
        yield '%s %s' % (gender, month), 1

    def sum_births(self, month, births):
        yield month, sum(births)

    def steps(self):
        return [
            self.mr(mapper=self.filter_births_by_gender),
            self.mr(mapper=self.counter_mapper,
                    reducer=self.sum_births)
        ]


if __name__ == '__main__':
    MRFemaleBirthCounter.run()
