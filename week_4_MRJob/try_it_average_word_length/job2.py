from mrjob.job import MRJob


class Job(MRJob):

    def mapper(self, key, value):
        numCharacters = len(value.strip().replace(" ", ""))
        numWords = len(value.strip().split())
        yield "stats", (numCharacters, numWords)

    def reducer(self, key, values):
        totalCharacters = 0
        totalWords = 0
        for value in values:
            totalCharacters = totalCharacters + value[0]
            totalWords = totalWords + value[1]
        yield "Average word length", totalCharacters/totalWords


if __name__ == '__main__':
    Job.run()
