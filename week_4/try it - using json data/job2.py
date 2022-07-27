from mrjob.job import MRJob
import json


class Job(MRJob):

    def mapper(self, key, value):
        people = json.loads(value)
        for person in people:
            for course in person["courses"]:
                yield course, person["name"]

    def reducer(self, key, values):
        yield key, ', '.join(values)


if __name__ == '__main__':
    Job.run()
