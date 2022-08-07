from mrjob.job import MRJob


class Job(MRJob):
    def mapper(self, key, value):
        fields = value.strip().split(',')
        name = fields[-3] + ' ' + fields[-2]
        price, qty = float(fields[4]), int(fields[-4])
        yield name, (price, qty)

    def combiner(self, key, values):
        total_price, total_qty = 0, 0
        for value in values:
            total_price += (value[0] * value[1])
            total_qty += value[1]
        yield key, (total_price, total_qty)

    def reducer(self, key, values):
        total_price, total_qty = 0, 0
        for value in values:
            total_price += (value[0])
            total_qty += (value[1])
        average = round(total_price / total_qty, 2)
        yield key, average


if __name__ == '__main__':
    Job.run()

# python 4b.py orders.csv
