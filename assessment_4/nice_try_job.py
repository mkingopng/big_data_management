from mrjob.job import MRJob


class Job(MRJob):
    def __init__(self, args=None):
        super().__init__(args)
        self.freq = None

    def mapper(self, _, value):
        (year, words) = value.strip().split(",")
        date = (year[0:4])
        stopwords = {"to", "a", "an", "the", "for", "in", "on", "of", "at", "over", "with", "after", "and", "from",
                     "new", "us", "by", "as", "man", "up", "says", "out", "is", "be", "are", "not", "pm", "am", "off",
                     "more", "less", "no", "how"}

        word_list = words.split()
        word_list = ([words for words in word_list if words not in stopwords])

        yield date, word_list

    def reducer(self, year, values):
        # an empty dictionary for storing frequency of each word
        self.freq = {}

        # iterating values generator
        for value in values:
            # iterating through value v list
            for word in value:
                # if word doesn't in freq, adding word to v and incrementing count by 1
                if word not in self.freq:
                    self.freq[word] = 0
                self.freq[word] += 1

        # sorting freq dict by values, in decreasing order
        sorted_freq = sorted(self.freq.items(),
                             key=lambda item: (item[1], item[0]),
                             reverse=True)

        # extracting three most frequent words from sorted_freq list
        words = [word for word, freq in sorted_freq[:3]]

        # sorting the words
        words.sort()

        yield year, words


if __name__ == "__main__":
    Job.run()
