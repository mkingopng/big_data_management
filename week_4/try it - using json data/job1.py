from mrjob.job import MRJob
import json


class Job(MRJob):
    def mapper(self, key, value):
        people = json.loads(value)
        for person in people:
            for course in person["courses"]:
                yield "number", 1

    def reducer(self, key, values):
        yield "Total enrolments:", sum(values)


if __name__ == '__main__':
    Job.run()
