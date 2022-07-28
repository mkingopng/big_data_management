from mrjob.job import MRJob
class Job(MRJob):
    def mapper(self, key, value):
        # Insert your code here
    def reducer(self, key, values):
        # Insert your code here
if __name__ == '__main__':
    Job.run()
