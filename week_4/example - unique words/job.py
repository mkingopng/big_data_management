from mrjob.job import MRJob
class Job(MRJob):
    def mapper(self, key, value):
        for word in value.split():
            yield word, ""
    def reducer(self, key, values):
        yield key, ""
if __name__ == '__main__':
    Job.run()
